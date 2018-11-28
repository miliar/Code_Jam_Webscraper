#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std ;

int p[1010] ;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int _ , ca = 1 ;
    int d , i , t , j , l , flag , ans;
    scanf("%d",&_);
    p[0]=0;
    while(_--)
    {
        scanf("%d",&d);
        ans = -1 ;
        for ( i = 1 ; i <= d ; i++ )
        {
            scanf("%d",&p[i]);
            ans = max(ans,p[i]);
            p[i]--;
        }
        l = ans ;
        for ( i = 1 ; i < l ; i++ )
        {
            t = 0 ;
            for ( j = 1 ; j <= d ; j++ )
            {
                if ( p[j] > 0 )
                {
                   t += p[j] / i ;
                   if ( p[j] % i != 0 )t++ ;
                }
                p[j]-- ;
            }
            ans = min(ans,t+i);
        }
        printf("Case #%d: %d\n",ca++,ans);
    }
    return 0 ;
}
