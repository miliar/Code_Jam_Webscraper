#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std ;

char s[1010];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,ca=1;
    int n , i , sum , res ;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%s",&n,s);
        for ( i = sum = res = 0 ; i <= n ; i++ )
        {
            if ( i > sum + res )
            {
                res += i - sum - res ;
            }
            sum += s[i] - '0' ;
        }
        printf("Case #%d: %d\n",ca++,res);
    }
    return 0 ;
}
