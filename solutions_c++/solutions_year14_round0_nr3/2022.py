/*
 * Author:  Plumrain
 * Created Time:  2014-04-13 03:23
 * File Name: Ctst.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <sstream>
#include <fstream>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <cctype>
#include <ctime>
#include <utility>

using namespace std;

#define clr(x,y) memset(x, y, sizeof(x))
#define pb push_back
#define mp make_pair
#define x first
#define y second
#define sz(v) ((int)(v).size())
#define all(t) t.begin(),t.end()
#define INF 999999999999999999
#define zero(x) (((x)>0?(x):-(x))<eps)
#define repf(i, a, b) for(int i = (a); i <= (int)(b); i ++)
#define repd(i, a, b) for(int i = (a); i >= (int)(b); i --)
#define out(x) cout<<#x<<":"<<(x)<<endl
#define tst(a) cout<<a<<" "
#define tst1(a) cout<<#a<<endl
#define CINBEQUICKER std::ios::sync_with_stdio(false)

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef pair<int, int> pii;

const double eps = 1e-10;
const double PI = atan(1.0)*4;
const int inf = 2147483647 / 2;

template <class T> void chmin(T &t,T x){if (x < t) t = x;}
template <class T> void chmax(T &t,T x){if (x > t) t = x;}

int n, m;
string an;
char s[1000];
int num[55][55];
vs bod;
bool v[55][55], col[55][55];
bool newout[55][55];

int calc(int cn, int cm){
    int ret = 0;
    repf (i, max(0,cn-1), min(cn+1,n))
        repf (j, max(0,cm-1), min(cm+1,m))
            if (v[i][j]) ++ ret;
    return ret;
}

void color(int x, int y){
    col[x][y] = 1;
    if (num[x][y] != 0) return;
    repf (i, max (1,x-1), min(n,x+1)) repf (j, max(1,y-1), min(m,y+1)){
        if (!col[i][j]) color (i, j);
    }
}

int main()
{
    freopen("c.out","r",stdin);
    freopen("ans.out","w",stdout);
//    std::ios::sync_with_stdio(false);
    int T = 225, cas = 0;
    while (T--){
        int cnt;
        string stmp; cin >> stmp; 
        //cout << stmp << endl;
        cin >> n >> m >> cnt;
        //out (n); out (m); out (cnt);

        string an;
        cin >> an;
        if (!(an == "Impossible")){
            bod.clear(); bod.pb ((string)"");
            bod.pb(an);
            repf (i, 2, n) cin >> an, bod.pb (an);
            repf (i, 1, n) bod[i] = "a" + bod[i];

            pii stat;
            repf (i, 1, n) repf (j, 1, m){
                if (bod[i][j] == 'c') stat.x = i, stat.y = j, v[i][j] = 0;
                else if (bod[i][j] == '.') v[i][j] = 0;
                else v[i][j] = 1;
            }

            //if (n == 2 && m == 4 && cnt == 4){
                //repf (i, 1, n) {repf (j, 1, m) cout << v[i][j];
                    //cout << endl;
                //}
                //out (stat.x); out (stat.y);
            //}
           // 
            clr (col, 0);
            repf (i, 1, n) repf (j, 1, m) num[i][j] = calc (i, j);
            color (stat.x, stat.y);

            //if (n == 2 && m == 4 && cnt == 4){
                //repf (i, 1, n) {repf (j, 1, m) cout << num[i][j];
                    //cout << endl;
                //}
                //out (stat.x); out (stat.y);
            //}
//
            bool ans = 1;
            repf (i, 1, n) repf (j, 1, m) if (!col[i][j] && !v[i][j]) ans = 0;
            if (!ans){
                cout << stmp << endl;
                cout << n << " " << m << " " << cnt << endl;
                printf ("NO\n");
            }
            else {
                //printf ("YES\n");
                continue;
            }
        }

        bool ans = 0;
        int tot = n * m, tsta;
        pii idx;
        repf (sta, 1, (1<<tot)-1) if (__builtin_popcount(sta) == cnt){
            repf (i, 1, n) repf (j, 1, m) v[i][j] = sta & (1<<(j-1 + m*(i-1)));
            repf (i, 1, n) repf (j, 1, m) num[i][j] = calc (i, j);

            repf (i, 1, n) repf (j, 1, m) if (!v[i][j]){
                clr (col, 0);
                color (i, j);

                bool u = 1;
                if (sta == 30309375) tst (i), tst (j), out (col[3][1]);
                repf (ii, 1, n) repf (jj, 1, m) if (!col[ii][jj] && !v[ii][jj]){
                    u = 0; break;
                }
                if (u){
                    ans = 1, tsta = sta, idx = mp (i, j); out (sta);
                    repf (ii, 1, n) repf (jj, 1, m) newout[ii][jj] = v[i][j];
                    break;
                }
            }
            if (ans) break;
        }
        if (ans){ printf ("NO\n");
            cout << n << " " << m << " " << cnt << endl;
            repf (i, 1, n){
                repf (j, 1, m){
                    if (idx.x == i && idx.y == j) printf ("c");
                    else if (v[i][j]) printf ("*");
                    else printf (".");
                }
                printf ("\n");
            }
        }
        else printf ("YES\n");
    }
    return 0;
}
