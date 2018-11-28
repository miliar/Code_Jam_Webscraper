#include<bits/stdc++.h>

using namespace std;

int dp[10009];
inline void test(void)
{
    repe(i,1,3)
        dp[i] = i;
    rep(i, 4, 1008)
        {
            if(i%3 == 0)
                dp[i] = dp[i/3] + 1;
            else
                dp[i] = max(dp[i/3+1], dp[i/2])+1;
        }
}

int main()
{
  
       cout <<"Case #" <<_cases <<": " << answer <<"\n";

    }
    return 0;
}
