#ifdef SHTRIX 
#include "/Users/roman/Dev/SharedCpp/DebugOutput.h"
#endif
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <sstream>
#include <map>
#include <set>
#include <stack>
#include <cstring>
#include <ctime>
#include <cstdio>
#include <cassert>
#include <memory>
using namespace std;
#define pb push_back
#define INF 1000000000
#define L(s) (int)((s).end()-(s).begin())
#define FOR(i,a,b) for (int i = (a); i <= (b); i++)
#define FORD(i,a,b) for(int i = (a); i >= (b); i--)
#define rep(i,n) FOR(i,1,(n))
#define rept(i,n) FOR(i,0,(n)-1)
#define C(a) memset((a),0,sizeof(a))
#define ll long long
#define all(c) (c).begin(), (c).end()
#define SORT(c) sort(all(c))
#define VI vector<int>
#define ppb pop_back
#define mp make_pair
#define pii pair<int,int>
#define pdd pair<double,double>
//#define x first
//#define y second
#define sqr(a) (a)*(a)
#define D(a,b) sqrt(((a).x-(b).x)*((a).x-(b).x)+((a).y-(b).y)*((a).y-(b).y))
#define pi 3.1415926535897932384626433832795028841971
#define UN(v) sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())

int used[5][5], b[5][5], t[5][5], r, c;
int dx[] = {0, 1, 0, -1, 1, -1, -1, 1};
int dy[] = {1, 0, -1, 0, -1, 1, -1, 1};

int check(int sx, int sy) {
    if (b[sx][sy]) return 0;

    used[sx][sy] = true;
    if (t[sx][sy]) return 1;
    int res = 1;
    rept(k, 8) {
        int qx = sx + dx[k], 
            qy = sy + dy[k];
        if (qx < 0 || qx >= r) continue;
        if (qy < 0 || qy >= c) continue;
        if (b[qx][qy]) continue;
        if (used[qx][qy]) continue;
        res += check(qx, qy);
    }
    return res;
}

void solve(int case_id) {
    cerr << case_id << endl;
    int m;
    scanf("%d%d%d", &r, &c, &m);
    int f = r * c - m;
    if (f == 1) {
        printf("Case #%d:\n", case_id); 
        rept(i, r) {
            rept(j, c) {
                if (i == 0 && j == 0) printf("c");
                else printf("*");
            }
            puts("");
        } 
        return;
    }
    int ci, cj;
    bool ok = false;
    rept(mask, (1 << (r * c))) {
        if (__builtin_popcount(mask) != m) continue;
        C(b);
        C(t);
        C(used);
        rept(i, r)
            rept(j, c) {
                if (mask & (1 << (i * c + j))) {
                    b[i][j] = 1;
                }
            }
        rept(i, r)
            rept(j, c) {
                if (b[i][j]) continue;
                t[i][j] = 0;
                rept(k, 8) {
                    int qx = i + dx[k], qy = j + dy[k];
                    if (qx < 0 || qx >= r) continue;
                    if (qy < 0 || qy >= c) continue;
                    if (b[qx][qy]) t[i][j]++;                
                }
            }
        rept(i, r)
            rept(j, c)
                if (t[i][j] == 0 && !b[i][j]) {
                    if (check(i, j) == f) {
                        ok = true;
                        ci = i;
                        cj = j;
                    }
                    
                    i = j = INF;

                    break;
                }
        if (ok) break;
    }
    printf("Case #%d:\n", case_id);
    if (!ok) puts("Impossible");
    else {
        C(used);
        rept(i, r) {
            rept(j, c) {
                if (b[i][j]) printf("*");
                else
                if (i == ci && j == cj) printf("c");
                else printf(".");
            }
            puts("");
        }
    }
}

int main()
{
    #ifdef SHTRIX 
    freopen("input.txt","rt",stdin); 
    //freopen("output.txt","wt",stdout); 
    #endif
	int TC;
    scanf("%d", &TC);
    rep(tc, TC) {
        solve(tc);
    }
    return 0;
}
