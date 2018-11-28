#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef pair <int,int> ii;
int dp[200][2];
char s[200];
void Solve(int TestCase);
int main()
{
    freopen("C:\\Users\\dell\\Downloads\\inputb.txt","r",stdin);
    freopen("C:\\Users\\dell\\Downloads\\outputb.txt","w",stdout);
    int tc,t;
    scanf("%d",&tc);
    for(t = 1 ; t<=tc ; t++) Solve(t);
    return 0;
}
void Solve(int TestCase)
{

    scanf("%s",s+1);
    int n = strlen(s+1);
    for(int i = 1 ; i<=n ; i++)
    {
        if(s[i] == '+')
        {
            dp[i][0] = dp[i-1][0];
            dp[i][1] = 1 + dp[i-1][0];
        }
        else
        {
            dp[i][0] = 1 + dp[i-1][1];
            dp[i][1] = dp[i-1][1];
        }
    }
    printf("Case #%d: %d\n",TestCase,dp[n][0]);
}

