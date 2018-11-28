#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <map>
#include <stack>
#include <queue>
#include <set>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <climits>
#include <cfloat>
#include <cstdlib>

#ifdef _WIN32
#define LLD "%I64d"
#else
#define LLD "%lld"
#endif

using namespace std;

#define pb push_back
#define mp make_pair
#define fs first
#define sc second

#define ri(X) scanf("%d", &(X))
#define rii(X, Y) scanf("%d%d", &(X), &(Y))
#define riii(X, Y, Z) scanf("%d%d%d", &(X), &(Y), &(Z))
#define all(a) (a).begin(),(a).end()
#define sz(s) ((int) ((s).size()))
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define fornr(i, n) for (int i = (int)(n)-1; i>=0; --i)
#define for1(i, n) for (int i = 1; i <= (int)(n); ++i)
#define for1r(i, n) for (int i = (int)(n); i>0; --i)

#define INF 0x3f3f3f3f
#define INFL 0x3f3f3f3f3f3f3f3fLL

typedef pair<int,int> pii;
typedef vector<int> vi;
typedef long long ll;
typedef vector<ll> vll;

int mod1 = int(1e9) + 7;

#define MX 100100

double p[20];

double dp[70000][40];

void main2(){

    int n,k;
    rii(n,k);

    for1(i,n)
        scanf("%lf", &p[i]);

    memset(dp,0,sizeof(dp));

    int offset = 20;
    dp[0][0 + offset] = 1;

    for1(r,n) {
        for(int mask=0; mask<(1<<(r-1)); mask++) {
            for(int b=-r; b<=r; b++) {
                dp[mask + (1<<(r-1))][b+offset] = dp[mask][b-1+offset] * p[r] + dp[mask][b+1+offset] * (1.0-p[r]);
            }
        }
    }
    double ans = 0;
    for(int mask=((1<<k)-1);mask<(1<<n);mask++) {
        int cnt = 0;
        for(int i=0; i<20; i++) {
            cnt += (mask & (1<<i))>0;
        }
        if(cnt==k) {
            ans = max(ans, dp[mask][offset]);
        }
    }

    printf("%.8f\n", ans);
}


int main(){

    int t;
    ri(t);

    for1(cas,t) {
        printf("Case #%d: ", cas);
        main2();
    }

    return 0;
}
