#include<cstdio>

int main()
{
    int t;
    scanf("%d",&t);
    for(int x=1;x<=t;x++)
    {
        printf("Case #%d: ",x);
        int a,b;
        bool r[2][4][17]={false};
        scanf("%d",&a);
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                int tmp;
                scanf("%d",&tmp);
                r[0][i][tmp] = true;
            }
        }
        scanf("%d",&b);
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                int tmp;
                scanf("%d",&tmp);
                r[1][i][tmp] = true;
            }
        }
        int ans = 0;
        for(int i=1;i<=16;i++)
        {
            if(r[0][a-1][i] && r[1][b-1][i])
            {
                if(ans != 0)
                {
                    ans = -1;
                }
                else
                {
                    ans = i;
                }
            }
        }
        if(ans == 0)
        {
            printf("Volunteer cheated!\n");
        }
        else if(ans>0)
        {
            printf("%d\n",ans);
        }
        else
        {
            printf("Bad magician!\n");
        }
    }
    return 0;
}
