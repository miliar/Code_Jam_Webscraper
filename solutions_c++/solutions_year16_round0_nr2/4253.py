#include <bits/stdc++.h>

using namespace std;

#define FILE_IO

char s[105];
int dp[2005];
queue <int> q;

int main()
{
    #ifdef FILE_IO
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    #endif

    int T;
    scanf("%d\n", &T);
    for(int test = 1; test <= T; test++)
    {
        gets(s);
        int N = strlen(s);
        int msk = 0;
        for(int i = 0; i < N; i++)
            if(s[i] == '+')
                msk |= (1 << i);

        memset(dp, 0, sizeof(dp));
        dp[msk] = 1;
        q.push(msk);
        while(!q.empty())
        {
            int msk = q.front();
            q.pop();
            for(int i = 0; i < N; i++)
            {
                int newmsk = ((1 << (i + 1)) - 1) ^ msk;
                if(dp[newmsk])  continue;
                dp[newmsk] = dp[msk] + 1;
                q.push(newmsk);
            }
        }
        printf("Case #%d: %d\n", test, dp[(1 << N) - 1] - 1);
    }

    return 0;
}
