#include<cstdio>
#include<algorithm>
#include<cstring>

using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.txt","w",stdout);
    int n;
    int dp[110][2];
    char str[110];
    scanf("%d",&n);
    for ( int d=1 ; d<=n ; d++ )
    {
        scanf("%s",str+1);
        int l = strlen(str+1);
        dp[1][0] = dp[1][1] = 0;
        if ( str[1] == '+' ) dp[1][1]++;
        else dp[1][0]++;
        for ( int c=2 ; c<=l ; c++ )
        {
            if ( str[c] == '+' )
            {
                dp[c][0] = dp[c-1][0];
                dp[c][1] = dp[c-1][0] + 1;
            }
            else
            {
                dp[c][0] = dp[c-1][1]+1;
                dp[c][1] = dp[c-1][1];
            }
        }
        printf("Case #%d: %d\n",d,dp[l][0]);
    }
}
