#include<stdio.h>
int a[8][8],b[8][8];
int main()
{
    int t,i,j,res,n,m,cou,cas=1;

    //freopen("A-small-attempt1.in","r",stdin);
    //freopen("out.txt","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
                scanf("%d",&a[i][j]);
        }
        scanf("%d",&m);
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
                scanf("%d",&b[i][j]);
        }
        cou=res=0;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                if(a[n][i]==b[m][j]) res=a[n][i],cou++;
            }
        }
        printf("Case #%d: ",cas++);
        if(cou==0) printf("Volunteer cheated!\n");
        else if(cou==1) printf("%d\n",res);
        else printf("Bad magician!\n");
    }

    return 0;
}
