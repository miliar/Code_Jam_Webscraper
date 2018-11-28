#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <stack>
#include <utility>
#include <functional>
#include <ctime>
#include <cstdlib>
#include <string>
#include <cstring>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define pii pair<int,int>
#define pdd pair<double,double>
#define pll pair<ll,ll>
#define forn(i,a,b) for( int i = (a); i < (b); i++ )
#define rep(i,n) forn(i,0,n)
#define repe(i,n) for( i = 0; i < (n); i++ )

const int MXN = 110;
const int MXS = 20*10;
const int inf = 2e9;
const int mod = 1000000007;
const double eps = 1e-9;

int di [] = {-1,0,1,0};
int dj [] = {0,1,0,-1};

char mpp [MXN][MXN];

int dir( char c ){
    if(c=='^') return 0;
    if(c=='>') return 1;
    if(c=='v') return 2;
    if(c=='<') return 3;
}
char chrr ( int q ){
    if(q==0) return '^';
    if(q==1) return '>';
    if(q==2) return 'v';
    if(q==3) return '<';

}

int res = 0;
bool ok = true;

int n,m;

bool was [MXN][MXN];

int dfs( int i, int j, int dr, bool fst = false ){
    if(i<0 || j<0 || i>=n || j>=m) return 0;
    if(was[i][j]) return 1;
    if(mpp[i][j]!='.'){
        dr = dir(mpp[i][j]);
        was[i][j] = 1;
    }
    int q = dfs(i+di[dr], j+dj[dr], dr );
    if(q==0){
        if(fst || mpp[i][j]=='.') return 0;
        res++;
        return 1;
    }
    else return 1;
}

void solve(){
    rep(i,MXN) rep(j,MXN) was[i][j] = 0;

    scanf("%d%d", &n, &m);
    rep(i,n) scanf("%s", mpp[i]);

    res = 0;
    ok = true;

    rep(i,n){
        rep(j,m){
            if(mpp[i][j]!='.' && !was[i][j]){
                int dr = dir(mpp[i][j]);
                if( !dfs(i,j, dir(mpp[i][j]), true ) ){
                    res++;
                    bool kk = false;
                    rep(k,3){
                        dr = (dr+1)%4;
                        mpp[i][j] = chrr(dr);
                        was[i][j] = false;
                        kk |= dfs(i,j,dr,true);
                    }
                    if(!kk) ok = false;
                }
                if(!ok) break;
            }
        }
        if(!ok) break;
    }
    if(ok) printf("%d\n", res);
    else printf("IMPOSSIBLE\n");
}

int main()
{
    freopen("input.txt", "r", stdin);    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    rep(i,t){
        printf("Case #%d: ", i+1);
        solve();
//        printf("\n");
    }

    return 0;
}
