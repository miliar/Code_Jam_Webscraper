#include<stdio.h>
#include<string.h>
#include<iostream>
#include<algorithm>
#include<math.h>
#include<map>
#include<vector>
#include<string>
#include<set>
#include<queue>
#define MP(x,y) make_pair(x,y)
#define clr(x,y) memset(x,y,sizeof(x))
#define forn(i,n) for(int i=0;i<n;i++)
#define sqr(x) ((x)*(x))
#define MAX(a,b) if(a<b) a=b;
#define ll long long
using namespace std;


double dp[205][405];
double p[205];
int k, n;

double gao(int pre, int last)
{
    vector<double> a;
    for(int i = 0; i < pre; i++) a.push_back(p[i]);
    for(int i = n - last; i < n; i++) a.push_back(p[i]);

    clr(dp, 0);
    dp[0][200] = 1;
    for(int i = 0; i < k; i++)
    {
        for(int j = 200 - k; j <= 200 + k; j++)
        {
            dp[i + 1][j - 1] += dp[i][j] * (1 - a[i]);            
            dp[i + 1][j + 1] += dp[i][j] * a[i];
        }
    }
    return dp[k][200];
}

int main() {
    freopen("in","r",stdin);
    freopen("out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; cas++)
    {
        scanf("%d%d", &n, &k);          
        for(int i = 0; i < n; i++) scanf("%lf", &p[i]);
        sort(p, p + n);

        double ans = 0;
        for(int i = 0; i <= k; i++)
        {
            ans = max(ans, gao(i, k - i));
        }

        printf("Case #%d: %lf\n", cas, ans);
    }
    return 0;
}
