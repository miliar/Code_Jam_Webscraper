#include<cstdio>

int ar1[10][10],ar2[10][10],sum[100];
int main()
{
    int t,tt;
    scanf("%d",&tt);
    for(int t=0;t<tt;t++)
    {
        int a,b,tmp,chk=0;
        scanf("%d",&a);
        for(int i=1;i<=4;i++) for(int j=1;j<=4;j++) scanf("%d",&ar1[i][j]);
        scanf("%d",&b);
        for(int i=1;i<=4;i++) for(int j=1;j<=4;j++) scanf("%d",&ar2[i][j]);
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                if(ar1[a][i] == ar2[b][j])
                {
                    sum[t]=ar1[a][i];
                    chk++;
                }
            }
        }
        if(chk>1) sum[t]=-1;
        else if(chk==0) sum[t]=-2;
    }
    for(int t=0;t<tt;t++)
    {
        printf("Case #%d: ",t+1);
        if(sum[t]== -2) printf("Volunteer cheated!\n");
        else if(sum[t] == -1) printf("Bad magician!\n");
        else printf("%d\n",sum[t]);
    }
}
