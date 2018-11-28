#include<stdio.h>
int row [5];
int expected[5];
int main ()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("MagicTrick.out","w",stdout);
    int t;
    scanf("%d",&t);
    int T=1;
    while (t--)
    {
        int f,s;
        int num;
        int cnt =0;
        scanf("%d",&f);
        for (int i=1;i<=4;i++)
        {
            for (int j=0;j<4;j++)
            {
                scanf ("%d",&num);
                if (i==f)
                    row[j] = num;
            }
        }
        bool flag;
        scanf ("%d",&s);
        for (int i=1;i<=4;i++)
        {
            for (int j=0;j<4;j++)
            {
                scanf ("%d",&num);
                if (i==s){
                    flag =0;
                    for (int k=0;k<4;k++)
                    {
                        if (row[k]== num)
                            flag =1;
                    }
                    if (flag)
                       expected[cnt++] = num;
                }
            }
        }
//        if (cnt )
        printf("Case #%d: ",T++);
        if (cnt ==0)
            printf("Volunteer cheated!\n");
        else if (cnt==1)
            printf("%d\n",expected[0]);
        else
            printf("Bad magician!\n");
    }
}
