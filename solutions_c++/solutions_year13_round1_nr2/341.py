#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <cstdlib>
#include <cmath>
using namespace std;

const int MAXE = 7, MAXN = 10010;
long long dp[2][MAXE];
long long val[MAXN];

int main()
{
    int TC, N;
    cin>>TC;

    for(int tc = 1; TC--; ++tc)
    {
        long long R, E;
        cin>>E>>R>>N;
        for(int i = 0; i < N; i++)
            cin>>val[i];

        memset(dp, -1, sizeof(dp));
        dp[0][E] = 0;
        for(int i = 0; i < N; i++)
        {
            memset(dp[1], -1, sizeof(dp[1]));

            for(int j = 0; j <= E; j++)
                if(dp[0][j] != -1)
                {
                  //  cout<<"GGGG "<<i<<' '<<j<<endl;
                    for(int k = 0; k <= j; k++)
                        dp[1][min(E, j-k+R)] = max(dp[1][min(E, j-k+R)], dp[0][j]+k*val[i]);
                }
           /* cout<<"WHY "<<endl;
            for(int j = 0; j <= E; j++)
                cout<<"DEBUG "<<j<<' '<<dp[1][j]<<endl;*/
            memcpy(dp[0], dp[1], sizeof(dp[0]));
        }
        
        long long ans = 0;
        for(int i = 0; i <= E; i++)
            ans = max(ans, dp[0][i]);
        printf("Case #%d: %lld\n", tc, ans);
    }
}
