#include <cstdio>
#include<cstring>
using namespace std;
int card,k,row,t,jj,i,j,v[20],w[7],a[7][7];
int main()
{
    freopen("mt.in","r",stdin);
    freopen("mt.out","w",stdout);
    scanf("%d",&t);
    j=0;
    while(t>0)
    {
        t--;
        jj++;
        k=0;
       memset(v,0,sizeof(v));
        scanf("%d",&row);
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                scanf("%d",&a[i][j]);
        for(i=1;i<=4;i++)
            v[a[row][i]]++;
        scanf("%d",&row);
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                scanf("%d",&a[i][j]);
        for(i=1;i<=4;i++)
            if(v[a[row][i]]==1)
            {
                k++;
                card=a[row][i];
            }
        if(k>1)
        printf("Case #%d: Bad magician!\n",jj);
        else if(k==1)
        printf("Case #%d: %d\n",jj,card);
        else printf("Case #%d: Volunteer cheated!\n",jj);
    }
    return 0;
}
