#include<cstdio>
#include<cstring>

int T;
int a[5][5],b[5][5];
int row1,row2;
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    scanf("%d",&T);
    for(int cases = 1;cases <= T;cases++)
    {
        printf("Case #%d: ",cases);

        scanf("%d",&row1);
        for(int i = 1;i <= 4;i++)
        {
            for(int j = 1;j <= 4;j++)scanf("%d",&a[i][j]);
        }
        scanf("%d",&row2);
        for(int i = 1;i <= 4;i++)
        {
            for(int j = 1;j <= 4;j++)scanf("%d",&b[i][j]);
        }
        int tot = 0;
        int ans;
        for(int i = 1;i <= 4;i++)
        {
            int aa = a[row1][i];
            for(int j = 1;j <= 4;j++)
            {
                int bb = b[row2][j];
                if(aa == bb){ans = aa;tot++;break;}
            }
        }
        if(tot == 1)
        {
            printf("%d\n",ans);
        }
        else if(tot == 0)
        {
            printf("Volunteer cheated!\n");
        }
        else printf("Bad magician!\n");
    }
    return 0;
}
