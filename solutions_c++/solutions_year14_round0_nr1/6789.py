#include<cstdio>
#include<cstring>
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int FLAG[20];
    int T;
    scanf("%d",&T);
    for(int E=1;E<=T;E++)
    {
        memset(FLAG,0,sizeof(FLAG));
        int a,b;
        int x[5][5],y[5][5];
        scanf("%d",&a);
        for (int i=1;i<=4;i++)
            for (int j=1;j<=4;j++)
                scanf("%d",&x[i][j]);
        scanf("%d",&b);
        for (int i=1;i<=4;i++)
            for (int j=1;j<=4;j++)
                scanf("%d",&y[i][j]);
        for (int i=1;i<=4;i++)
            for (int j=1;j<=4;j++)
                if (x[a][i]==y[b][j])
                    FLAG[x[a][i]]=1;
        int _count=0,emm=0;
        for (int i=1;i<=16;i++)
            if (FLAG[i]==1)
            {
                _count++;
                emm=i;
            }
        if (_count==0)
            printf("Case #%d: Volunteer cheated!\n",E);
        if (_count>1)
            printf("Case #%d: Bad magician!\n",E);
        if (_count==1)
            printf("Case #%d: %d\n",E,emm);
    }
    fclose(stdout);
}
