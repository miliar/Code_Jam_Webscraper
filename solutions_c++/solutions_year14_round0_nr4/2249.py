#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std ;

double n1[1010],n2[1010];
int vis [1010];
int main()
{
    freopen("D-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int _,ca=1;
    int n;
    int i ,l1,l2,j;
    scanf ("%d", &_);
    while(_--)
    {
        scanf("%d",&n);
        for ( i = 0 ; i < n ; i++ )
            scanf("%lf",&n1[i]);
        for(i = 0 ; i < n ; i++)
            scanf ("%lf",&n2[i]);

        sort(n1,n1+n);
        sort(n2,n2+n);
        l1 = l2 = 0 ;
        for ( i = j = 0 ; i < n ; i++ )
        {
            if ( n1[i]>n2[j] )
            {
                l1++;
                j++;
            }
        }
        memset(vis,0,sizeof(vis));
        for ( j = 0 , i = 0 ; i < n && j < n; i++ )
        {
            while ( j < n )
            {
                if ( n2[j]>n1[i] )
                {
                    l2++;
                    j++ ;
                    break ;
                }
                else j++;
            }
        }
        printf("Case #%d: %d %d\n",ca++ , l1,n-l2);
    }
    return 0 ;
}
