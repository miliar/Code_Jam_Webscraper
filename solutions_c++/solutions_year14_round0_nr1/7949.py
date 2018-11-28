#include<stdio.h>
int num[5][5],ans[5];
int main()
{
    int t,n,i,j,res;
    int cas=1;
    freopen("A-small-attempt3.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                scanf("%d",&num[i][j]);
        int k=1;
        for(i=1;i<=4;i++)
            ans[k++]=num[n][i];
        scanf("%d",&n);
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                scanf("%d",&num[i][j]);
        int flag=0;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
                if(num[n][i]==ans[j])
                {
                    flag++;
                    res=ans[j];
                    break;
                }
            if(flag>1)
                break;
        }
        printf("Case #%d: ",cas++);
        if(flag==1)
            printf("%d\n",res);
        else if(flag==0)
            printf("Volunteer cheated!\n");
        else
            printf("Bad magician!\n");
    }
    return 0;
}
