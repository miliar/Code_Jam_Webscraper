#include <stdio.h>
using namespace std;

long long int n;
void solve()
{

    int k,c,s;
    scanf("%d %d %d\n",&k,&c,&s);
    for (int i=1;i<=k;i++) printf("%d ",i);
    printf("\n");
    return ;

    if ( c==1 )
    {
        if ( s < k ) printf("IMPOSSIBLE");
        else for (int i=1;i<=k;i++) printf("%d ",i);
        printf("\n");
        return;
    }

    if ( c*s < k )
    {
        printf("IMPOSSIBLE\n");
        return;
    }
    for (long long int i=0;i<s;i++)
    {
        long long int ans =0;
        for (long long int j=c-1;j>=0;j--)
            ans = k*ans + (i*c + j);
        printf("%lld ",ans);
    }
    printf("\n");
}

int main()
{
    int T;
    printf("\n");
    scanf("%d",&T);
    for (int t=1;t<=T;t++)
    {
        printf("Case #%d: ",t);
        solve();
    }
    return 0;
}
