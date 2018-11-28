//Coder: Balajiganapathi
#ifndef ONLINE_JUDGE
#   define DEBUG
#   define TRACE
#else
//#   define NDEBUG
#endif

#include <algorithm>
#include <bitset>
#include <deque>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

typedef vector<int> vi;
typedef pair<int,int> pi;
typedef vector<string> vs;
typedef vector<pi> vpi;

// Basic macros
#define fi          first
#define se          second
#define all(x)      (x).begin(), (x).end()
#define ini(a, v)   memset(a, v, sizeof(a))
#define re(i,s,n)  	for(int i=s;i<(n);++i)
#define rep(i,s,n)  for(int i=s;i<=(n);++i)
#define fo(i,n)     re(i,0,n)
#define rev(i,n,s)  for(int i=(n)-1;i>=s;--i)
#define repv(i,n,s) for(int i=(n);i>=s;--i)
#define fov(i,n)    rev(i,n,0)
#define pu          push_back
#define mp          make_pair
#define si(x)       (int)(x.size())

#ifdef TRACE
    #define trace(x)            cerr<<x<<endl;
    #define trace1(x)           cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<endl;
    #define trace2(x,y)         cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<" | "#y" = "<<y<<endl;
    #define trace3(x,y,z)       cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<" | "#y" = "<<y<<" | "#z" = "<<z<<endl;
    #define trace4(a,b,c,d)     cerr<<__FUNCTION__<<":"<<__LINE__<<": "#a" = "<<a<<" | "#b" = "<<b<<" | "#c" = "<<c<<" | "#d" = "<<d<<endl;
    #define trace5(a,b,c,d,e)   cerr<<__FUNCTION__<<":"<<__LINE__<<": "#a" = "<<a<<" | "#b" = "<<b<<" | "#c" = "<<c<<" | "#d" = "<<d<<" | "#e" = "<<e<<endl;
    #define trace6(a,b,c,d,e,f) cerr<<__FUNCTION__<<":"<<__LINE__<<": "#a" = "<<a<<" | "#b" = "<<b<<" | "#c" = "<<c<<" | "#d" = "<<d<<" | "#e" = "<<e<<" | "#f" = "<<f<<endl;
#else
    #define trace(x)
    #define trace1(x)
    #define trace2(x,y)
    #define trace3(x,y,z)
    #define trace4(a,b,c,d)
    #define trace5(a,b,c,d,e)
    #define trace6(a,b,c,d,e,f)
#endif

const int oo = 1000000009;
const double eps = 1e-6;
const int mod = 1000000007;
const int mx = 102;

char b[mx][mx];
int bd[mx][mx];
int n, m;
pi next[mx][mx];
vpi adj[mx][mx];

int di[] = {-1, 1, 0, 0}, dj[] = {0, 0, -1, 1};

bool isvalid(int i, int j) {
    return i >= 0 && i < n && j >= 0 && j < m;
}

bool isvalid(pi p) {
    return isvalid(p.fi, p.se);
}

int main() {
    //freopen("sample.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);

    //freopen("A-small-attempt1.in", "r", stdin);
    //freopen("small1.txt", "w", stdout);

    freopen("A-large.in", "r", stdin);
    freopen("large.txt", "w", stdout);
    
    int kases;
    scanf("%d", &kases);
    for(int kase = 1; kase <= kases; ++kase) {
        scanf("%d %d", &n, &m);
        fo(i, n) scanf("%s", b[i]);
        ini(bd, -1);
        fo(i, n) fo(j, m) {
            if(b[i][j] == '^') bd[i][j] = 0;
            else if(b[i][j] == 'v') bd[i][j] = 1;
            else if(b[i][j] == '<') bd[i][j] = 2;
            else if(b[i][j] == '>') bd[i][j] = 3;
            if(b[i][j] == '.') continue;

            for(next[i][j] = mp(i + di[bd[i][j]], j + dj[bd[i][j]]); isvalid(next[i][j]) && b[next[i][j].fi][next[i][j].se] == '.'; ) {
                next[i][j].fi += di[bd[i][j]];
                next[i][j].se += dj[bd[i][j]];
            }
            if(!isvalid(next[i][j])) {
                fo(d, 4) {
                    pi cur(i + di[d], j + dj[d]);
                    for(; isvalid(cur) && b[cur.fi][cur.se] == '.'; cur = mp(cur.fi + di[d], cur.se + dj[d]));
                    if(isvalid(cur)) adj[i][j].pu(cur);
                }
            }
            //trace4(i, j, next[i][j].fi, next[i][j].se);
        }

        bool possible = true;
        int ans = 0;
        fo(i, n) fo(j, m) if(bd[i][j] != -1 && !isvalid(next[i][j])) {
            if(si(adj[i][j]) == 0) {
                possible = false;
                break;
            }
            ++ans;
        }
        printf("Case #%d: ", kase);
        if(possible) printf("%d\n", ans);
        else printf("IMPOSSIBLE\n");
        fo(i, n) fo(j, m) adj[i][j].clear();
    }
    
	return 0;
}
