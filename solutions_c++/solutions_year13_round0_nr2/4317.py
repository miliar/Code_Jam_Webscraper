#include<stdio.h>
#include<string.h>
int maxR[110],maxC[110],nCases,val[110][110],r,c,cant;
int main (void)
{
    freopen("input","r",stdin);
    freopen("output","w",stdout);
    scanf("%d",&nCases);
    for(int i=1;i<=nCases;i++)
    {
        scanf("%d%d",&r,&c);
        cant=0;
        memset(maxR,0,sizeof(maxR));
        memset(maxC,0,sizeof(maxR));
        for(int j=0;j<r;j++)
        {
            for(int k=0;k<c;k++)
            {
                scanf("%d",&val[j][k]);
                if(val[j][k]>maxR[j])
                {
                    maxR[j]=val[j][k];
                }
                if(val[j][k]>maxC[k])
                {
                    maxC[k]=val[j][k];
                }
            }
        }
        for(int j=0;j<r;j++)
        {
            for(int k=0;k<c;k++)
            {
                if(val[j][k]<maxR[j]&&val[j][k]<maxC[k]&&!cant)
                {
                    printf("Case #%d: NO\n",i);
                    cant=1;
                }
            }
        }
        if(!cant)
        {
            printf("Case #%d: YES\n",i);
        }
    }
    return 0;
}
