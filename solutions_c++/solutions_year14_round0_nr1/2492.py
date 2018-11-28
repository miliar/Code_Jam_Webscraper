#include <cstdio>

int main()
{
    int T;
    freopen("in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d",&T);
    for(int cas = 1; cas <= T; cas++)
    {
        int ans1, ans2, rec1[5][5], rec2[5][5];
        scanf("%d",&ans1);
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                scanf("%d",&rec1[i][j]);
            }
        }
        scanf("%d",&ans2);
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                scanf("%d",&rec2[i][j]);
            }
        }
        int sum = 0;
        int num;
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                if(rec1[ans1][i] == rec2[ans2][j])
                {
                    sum ++;
                    num = rec1[ans1][i];
                    break;
                }
            }
        }
        printf("Case #%d: ", cas);
        if(sum == 0)
        {
            printf("Volunteer cheated!\n");
        }
        else if(sum == 1)
        {
            printf("%d\n",num);
        }
        else
        {
            printf("Bad magician!\n");
        }
    }
    return 0;
}
