#include <stdio.h>


int grid[3][7][7];

int main()
{
    freopen("A.in","rt",stdin);
    freopen("A.out","wt",stdout);
    int tst,cas;
    scanf("%d",&tst);
    for(cas=1;cas<=tst;cas++) {
        int r1,r2;
        scanf("%d",&r1);
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)   scanf("%d",&grid[0][i][j]);

        scanf("%d",&r2);
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)   scanf("%d",&grid[1][i][j]);

        int cnt = 0;
        int val;
        for(int i=1;i<=4;i++) {
            for(int j=1;j<=4;j++) {
                if(grid[0][r1][i] == grid[1][r2][j]) cnt++ , val = grid[0][r1][i];
            }
        }
        if(cnt==1) printf("Case #%d: %d\n",cas,val);
        else if(cnt>1) printf("Case #%d: Bad magician!\n",cas);
        else printf("Case #%d: Volunteer cheated!\n",cas);


    }

    return 0;
}
