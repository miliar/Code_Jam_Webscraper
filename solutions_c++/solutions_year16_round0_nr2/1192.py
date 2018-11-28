#include<cstdio>
#include<cstring>
#include<cstdlib>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    int _, ca=1;
    scanf("%d", &_);
    while (_--)
    {
        char s[200],x='+' ;
        int step = 0 ;
        int dp[200];
        scanf("%s", s);

        printf("Case #%d: ",ca++);
        dp[ strlen(s)] = 0;
        for (int i = strlen(s) - 1 ; i > -1 ; i--)
        {
            if ( x == s[i] )
            dp[i] = dp[i + 1];
            else
            {
                dp[i] = dp[i+1] + 1;
                if (x == '+')
                    x = '-';
                else
                    x = '+';
            }
        }
        printf("%d\n", dp[0]);
    }
    return 0;
}
