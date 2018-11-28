#include<cstdio>
#include<algorithm>

using namespace std;

double A[1010],B[1010];

int main()
{
    freopen("D-large.in","r",stdin);
    freopen("D-large.txt","w",stdout);
    int t,n;
    scanf("%d",&t);
    for ( int x=1 ; x<=t ; x++ )
    {
        scanf("%d",&n);
        for ( int c=1 ; c<=n ; c++ )    scanf("%lf",&A[c]);
        for ( int c=1 ; c<=n ; c++ )    scanf("%lf",&B[c]);
        sort ( A+1 , A+1+n );
        sort ( B+1 , B+1+n );
        int i=1,j=1,ans2=0;
        while ( j <= n )
        {
           if ( A[i] < B[j] )    i++,ans2++;
           j++;
        }
        //printf("%d\n",n-ans2);
        int ans=0;
        i=1,j=1;
        while ( i <= n )
        {
           if ( A[i] > B[j] )    j++,ans++;
           i++;
        }
        printf("Case #%d: %d %d\n",x,ans,n-ans2);
    }
}
