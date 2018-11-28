#include<stdio.h>
int main()
{
    int a[4][4],i,j,T,n,k,c;
    //freopen("H:A-small-attempt6.in","r",stdin);
    //freopen("A-small-attempt6.out","w",stdout);
    scanf("%d",&T);
    for(i=1;i<=T;i++)
    {
        printf("Case #%d: ",i);
        int b[20]={0};
        c=0;
        scanf("%d",&n);
        for(j=0;j<4;j++)
        for(k=0;k<4;k++)
        scanf("%d",&a[j][k]);
        for(j=0;j<4;j++)
        b[a[n-1][j]]=1;
        scanf("%d",&n);
         for(j=0;j<4;j++)
        for(k=0;k<4;k++)
        scanf("%d",&a[j][k]);
        for(j=0;j<4;j++)
        {
            if(b[a[n-1][j]]==1)
            {
                c++;
                k=a[n-1][j];
            }

        }
        if(c==0)
        printf("Volunteer cheated!\n");
        else if(c==1)
        printf("%d\n",k);
        else
        printf("Bad magician!\n");
    }
    return 0;
}
