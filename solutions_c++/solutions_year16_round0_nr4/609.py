#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("D large input.in","r",stdin);
    freopen("D large output.out","w",stdout);
    long long t,ti,m,n,s,i,j,k,ans;
    scanf("%lld",&t);
    for(ti=1;ti<=t;ti++)
    {
        scanf("%lld %lld %lld",&m,&n,&s);
        printf("Case #%lld: ",ti);
        if(m%n)
            if(m/n+1>s)
                printf("IMPOSSIBLE\n");
            else
            {
                for(i=0,k=1;i<m/n+1;i++)
                {
                    ans=k++;
                    for(j=0;j<n-1;j++,k++)
                        if(k<=m)
                            ans=(ans-1)*m+k;
                        else
                            ans*=m;
                    printf("%lld ",ans);
                }
                printf("\n");
            }
        else if(m/n>s)
            printf("IMPOSSIBLE\n");
        else
        {
            for(i=0,k=1;i<m/n;i++)
            {
                ans=k++;
                for(j=0;j<n-1;j++,k++)
                    if(k<=m)
                        ans=(ans-1)*m+k;
                    else
                        ans*=m;
                printf("%lld ",ans);
            }
            printf("\n");
        }
    }

}
