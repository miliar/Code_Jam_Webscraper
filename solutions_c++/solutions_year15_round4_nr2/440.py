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

void solve(){
    int n;
    double v,t;
    scanf("%d%lf%lf", &n, &v, &t);
    if(n==1){
        double r,t0;
        scanf("%lf%lf", &r, &t0);
        if(abs(t0-t)>1e-9){
            printf("IMPOSSIBLE");
            return;
        }
        else printf("%.9f", v/r);
    }
    else{
        double r0,t0,r1,t1;
        scanf("%lf%lf%lf%lf", &r0, &t0, &r1, &t1);
        if( abs(t0-t1)<1e-9 ){
            if(abs(t-t1)>1e-9) printf("IMPOSSIBLE");
            else{
                printf("%.9f", v/(r1+r0));
            }
        }
        else{
            double v0 = v*(t-t1)/(t0-t1);
            double v1 = v-v0;
            if(v0<0 || v1<0) printf("IMPOSSIBLE");
            else printf("%.9f", max(v0/r0, v1/r1));
        }
    }
}

int main()
{
    freopen("input.txt", "r", stdin);    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    rep(i,t){
        printf("Case #%d: ", i+1);
        solve();
        printf("\n");
    }
    return 0;
}
