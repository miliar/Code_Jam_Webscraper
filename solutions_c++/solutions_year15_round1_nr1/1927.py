#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std ;

int t[1010] ;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int _ , ca = 1 ;
    int n ;
    scanf("%d",&_);
    while(_--)
    {
        scanf("%d",&n);
        int ans1 = 0 , ans2 = 0 ;
        int ma = 0 ;
        for ( int i = 0 ; i < n ; i++ )
        {
            scanf("%d",&t[i]);
            if ( i && t[i] < t[i-1] )
            {
                ans1 += t[i-1] - t[i] ;
                ma = max(t[i-1]-t[i] ,ma);
            }
        }
        for ( int i = 0 ; i < n - 1 ; i++ )
        {
            if ( t[i] < ma ) ans2 += t[i] ;
            else ans2 += ma ;
        }
        printf("Case #%d: %d %d\n",ca++,ans1,ans2);
    }
    return 0 ;
}
