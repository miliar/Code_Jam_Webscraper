#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <climits>

using namespace std;

#define rep(i,a,b) for(int i = a; i < b; i++)
#define REP(i, n) for (int i = 0; i < (int)(n); ++i)
#define S(x) scanf("%d",&x)
#define P(x) printf("%d\n",x)

typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef long long LL;

const int MAXN = 1000010;
LL dp[MAXN];
int n;

LL solve(int x) {
    //cout<<x<<" ";

    LL &res = dp[x];
    if(res!=-1LL) return res;
    if(x==n) return res = 1LL;

    int rev=0, tx = x;
    while(tx) {
        rev = rev*10+tx%10;
        tx /= 10;
    }

    LL minn = 1 + solve(x+1);
    if(rev > x && rev <= n) minn = min(minn, 1 + solve(rev));
    return res = minn;
}

int main()
{
    freopen("A-small-attempt2.in","r",stdin);
    freopen("A-small2.out","w",stdout);

    int T;
    S(T);

    rep(t,1,T+1) {
        S(n);
        memset(dp, -1, sizeof(dp));

        printf("Case #%d: %d\n",t,solve(1));
    }
    return 0;
}
