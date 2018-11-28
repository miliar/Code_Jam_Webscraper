#include<bits/stdc++.h>
using namespace std;
int buck[3000];
int main()
{
    //freopen("C small input.in","r",stdin);
    //freopen("C small output.out","w",stdout);
    freopen("C large input.in","r",stdin);
    freopen("C large output.out","w",stdout);
    int t,ti,m,n,i,j,k,x;
    scanf("%d",&t);
    for(ti=1;ti<=t;ti++)
    {
        printf("Case #%d: ",ti);
        for(i=0;i<2600;i++)
            buck[i]=0;
        scanf("%d",&n);
        for(i=0;i<2*n-1;i++)
        {
            for(j=0;j<n;j++)
            {
                scanf("%d",&x);
                buck[x]++;
            }
        }
        for(i=0;i<=2500;i++)
            if(buck[i]%2)
                printf("%d ",i);
        printf("\n");
    }
}
