#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std ;
int a[1100] ;
double c[1100] ;
int main()
{
    int t , step = 0 ;
    int n , i , j ;
    double min1 ;
    freopen("AAA.in","r",stdin) ;
    freopen("AAA.out","w",stdout) ;
    scanf("%d", &t) ;
        while(t--)
        {
            scanf("%d", &n) ;
            for(i = 0 ; i < n ; i++)
                scanf("%d", &a[i]) ;
            int ans1 = 0 , ans2 = 0 ;
            for(i = 0 ; i < n-1 ; i++)
                if( a[i+1] < a[i] )
                    ans1 += (a[i]-a[i+1]) ;
            min1 = 0 ;
            for(i = 0 ; i < n-1 ; i++)
            {
                c[i] = 0 ;
                if( a[i] <= a[i+1] )
                    c[i] = 0 ;
                else
                {
                    c[i] += (a[i]-a[i+1])*1.0/10 ;
                }
                min1 = max(min1,c[i]) ;
            }
            for(i = 0 ; i < n-1 ; i++)
            {
                ans2 += min(min1*10,a[i]*1.0) ;
            }
            printf("Case #%d: %d %d\n", ++step, ans1, ans2) ;
    }
    return 0 ;
}
