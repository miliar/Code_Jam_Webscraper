#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
#include<string>
#include<stack>
#include<queue>

using namespace std;

int A,B;
int dp[1005];

bool chkpal(int x)
{
    int n= x;
    int d[4]={0};
    int cnt=0;
    while(n!=0)
    {
        d[cnt++] = n%10;
        n /= 10;
    }
    cnt--;
    for(int i=0;i<=cnt/2;i++)
    {
        if(d[i] != d[cnt - i])
            return false;
    }
    return true;
}

void caldp()
{
    dp[0] = 0;
    dp[1] = 1;
    for(int i=2;i<1005;i++)
    {
        if(chkpal(i))
        {
            bool sqr=false,fair=false;
            for(int j=0;j<=i/2;j++)
            {
                if(j*j == i)
                {
                    sqr = true;
                    fair = chkpal(j);
                    break;
                }
            }
            if(fair && sqr)
                dp[i] = dp[i-1]+1;
            else
                dp[i] = dp[i-1];
        }
        else
            dp[i] = dp[i-1];
    }    
}

int main()
{
    int T;
    caldp();
    cin >> T;
    for(int t=0;t<T;t++)
    {
        cin >>  A >> B;   
        printf("Case #%d: %d\n",t+1,dp[B] - dp[A-1]);
    }
    return 0;    
}
