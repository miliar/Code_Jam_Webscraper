#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("C large input.in","r",stdin);
	freopen("C large output.out","w",stdout);
    int t,m,n,i,j,k,cnt,cop;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%d %d",&m,&n);
        printf("Case #%d:\n",i);
        for(j=0,cnt=0;j<n;cnt++,j++)
        {
            printf("1");
            for(k=0,cop=cnt;k<m/2-1;k++,cop/=2)
                printf("%d%d",cop%2,cop%2);
            printf("1 ");
            for(k=3;k<=11;k++)
                printf("%d ",k);
            printf("\n");
        }
    }
}
