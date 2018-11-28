#include<stdio.h>
int main()
{
    freopen("A-small-attempt2.in","r",stdin);
    freopen("A-small-attempt2.out","w",stdout);
    int p[101][17]={},t,i,j,k,n,a[5][5],I[101],l[101];
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%d",&n);
        for(j=1;j<=4;j++)
        for(k=1;k<=4;k++)
        {
            scanf("%d",&a[j][k]);
            }
        for(k=1;k<=4;k++)
        {
            p[i][a[n][k]]++;
            }
        scanf("%d",&n);
        for(j=1;j<=4;j++)
        for(k=1;k<=4;k++)
        {
            scanf("%d",&a[j][k]);
            }
        for(k=1;k<=4;k++)
        {
            p[i][a[n][k]]++;
            }
        for(j=1;j<=16;j++)
        {
            if(p[i][j]==2)
            {
                I[i]=j;
                l[i]++;
                }
            }
        }
    for(i=1;i<=t;i++)
    {
        if(l[i]==1)
        {
            printf("Case #%d: %d\n",i,I[i]);
            }
        else if(l[i]==0)
        {
            printf("Case #%d: Volunteer cheated!\n",i);
            }
        else 
        {
            printf("Case #%d: Bad magician!\n",i);
            }
        }
    scanf(" ");
    }
