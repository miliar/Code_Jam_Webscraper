#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("inp.in", "r", stdin);
    freopen("outp.out", "w", stdout);
    int tc;
    scanf("%d", &tc);
    for(int kras=1; kras<=tc; kras++)
    {
        //ATTENTION! Check if the whitespace is needed or not before submitting!
        printf("Case #%d: ", kras);
        int n, k;
        scanf("%d %d", &n, &k);
        vector<double> p(n);
        for(int i=0; i<n; i++)
        {
            scanf("%lf", &p[i]);
        }

        double ans = 0.0;
        for(int bitmask=0; bitmask<(1LL<<n); bitmask++)
        {
            int aantal=0;
            vector<int> v;
            for(int i=0; i<n; i++)
            {
                if(1LL<<i&bitmask)
                {
                    aantal++;
                    v.push_back(i);
                }
            }
            if(aantal != k)
            {
                continue;
            }
            //groep is nu geselecteerd

            vector< vector<double> > dp(k, vector<double>(k/2+1, 0.0));
            dp[0][0] = 1-p[v[0]];
            dp[0][1] = p[v[0]];
            for(int i=1; i<k; i++)
            {
                dp[i][0]=1.0;
                for(int j=0; j<=i; j++)
                {
                    dp[i][0] *= (1-p[v[j]]);
                }
                for(int j=1; j<=k/2; j++)
                {
                    dp[i][j] = dp[i-1][j-1]*p[v[i]]+dp[i-1][j]*(1-p[v[i]]);
                }
            }
            ans = max(ans, dp[k-1][k/2]);

        }
        cout << fixed << setprecision(12) << ans << endl;

    }
    return 0;
}
