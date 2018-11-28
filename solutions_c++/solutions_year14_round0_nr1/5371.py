#include <stdio.h>

int first[4][4];
int second[4][4];
int frow[17];
int srow[17];

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int i,j,n,T,cnt=1,x,y;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d",&x);
        for (i=0;i<4;i++)
        {
            for (j=0;j<4;j++)
            {
                scanf("%d",&first[i][j]);
                frow[first[i][j]]=i;
            }
        }
        scanf("%d",&y);
        for (i=0;i<4;i++)
        {
            for (j=0;j<4;j++)
            {
                scanf("%d",&second[i][j]);
                srow[second[i][j]]=i;
            }
        }
        x--;y--;
        int ans=-1;
        for (i=1;i<=16;i++)
        {
            if (frow[i]==x && srow[i]==y)
            {
                if (ans!=-1) break;
                if (ans==-1) ans=i;
            }
        }
        printf("Case #%d: ",cnt++);
        if (ans==-1) printf("Volunteer cheated!\n");
        else if (i<=16) printf("Bad magician!\n");
        else printf("%d\n",ans);
    }
    return 0;
}
