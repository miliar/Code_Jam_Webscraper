#include <stdio.h>

int vis[17];
int a[5][5];

int main()
{
    int t;
    scanf("%d",&t);
    for (int l=1;l<=t;l++)
    {
        printf("Case #%d: ",l);
        for (int i=1;i<=16;i++) 
            vis[i] = 0;

        int ans1,ans2;
        scanf("%d",&ans1);
        for (int i=1;i<=4;i++)
            for (int j=1;j<=4;j++)
                scanf("%d",&a[i][j]);
        
        for (int j=1;j<=4;j++)
            vis[a[ans1][j]]++;

        scanf("%d",&ans2);
        for (int i=1;i<=4;i++)
            for (int j=1;j<=4;j++)
                scanf("%d",&a[i][j]);
        
        for (int j=1;j<=4;j++)
            vis[a[ans2][j]]++;

        int flag = 0;
        int ans;
        for (int i=1;i<=16;i++)
            if ( vis[i] == 2 ) 
            {
                flag++;
                ans = i;
            }
        if ( flag >= 2 )
            printf("Bad magician!\n");
        else if ( flag == 0 )
            printf("Volunteer cheated!\n");
        else
            printf("%d\n",ans);
    }
    return 0;
}
