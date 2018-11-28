#include<stdio.h>
int main()
{
    freopen("A-small-attempt3.in","r",stdin);
    freopen("A-small-attempt3.out","w",stdout);
    int T,a[5][5],b[5][5],cnt,flag,i,j,t,row1,row2;
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        scanf("%d",&row1);
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                scanf("%d",&a[i][j]);
        scanf("%d",&row2);
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                scanf("%d",&b[i][j]);
        cnt=0;
        flag=-1;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                if(a[row1][i]==b[row2][j])
                {
                    flag=a[row1][i];
                    cnt++;
                }
            }
        }
        if(cnt==0)printf("Case #%d: Volunteer cheated!\n",t);
        else if(cnt>1)printf("Case #%d: Bad magician!\n",t);
        else printf("Case #%d: %d\n",t,flag);
    }
    return 0;
}
