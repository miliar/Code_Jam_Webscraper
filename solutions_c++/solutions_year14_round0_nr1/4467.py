#include <cstdio>
#include <cstring>
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("1.txt","w",stdout);
    int anss,ans,d[17],i,j,t,_case,x,y,a[5][5],b[5][5];
    scanf("%d",&t);
    for (_case=1;_case<=t;_case++)
    {
        ans=0;
        memset(d,0,sizeof d);
        scanf("%d",&x);
        for (i=1;i<=4;i++)
            for (j=1;j<=4;j++)
            scanf("%d",&a[i][j]);
        for (i=1;i<=4;i++)
        d[a[x][i]]++;
        scanf("%d",&y);
        for (i=1;i<=4;i++)
            for (j=1;j<=4;j++)
            scanf("%d",&b[i][j]);
        for (i=1;i<=4;i++)
            d[b[y][i]]++;
        for (i=1;i<=16;i++)
        {
            if (d[i]==2)
            {
                anss=i;
                ans++;
            }
        }
        printf("Case #%d: ",_case);
        if (!ans)
            printf("Volunteer cheated!\n");
        else if  (ans==1)
            printf("%d\n",anss);
        else
            printf("Bad magician!\n");
    }
    return 0;
}
