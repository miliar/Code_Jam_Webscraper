#include <cstdio>
#include <cstdlib>

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T, cases;
    int i, j;
    char str[5]="\0";

    scanf("%d", &T);

    for(cases=1; cases<=T; ++cases)
    {
        int sum[10]={0};
        int done=1;
        int Ti=-1, Tj=-1;

        for(i=0; i<4; i++)
        {
            scanf("%s", str);
            for(j=0; j<4; j++)
                switch(str[j])
                {
                case 'O':
                    sum[i]++;
                    sum[4+j]++;
                    if(i==j)
                        sum[8]++;
                    if(i+j==3)
                        sum[9]++;
                    break;
                case 'X':
                    sum[i]--;
                    sum[4+j]--;
                    if(i==j)
                        sum[8]--;
                    if(i+j==3)
                        sum[9]--;
                    break;
                case 'T':
                    Ti = i;
                    Tj = j;
                    break;
                default:
                    done = 0;
                    break;
                }
        }

        if(Ti != -1)
            if(sum[Ti]==3)
            {
                printf("Case #%d: O won\n", cases);
                continue;
            }
            else if(sum[Ti]==-3)
            {
                printf("Case #%d: X won\n", cases);
                continue;
            }
            else if(sum[Tj+4]==3)
            {
                printf("Case #%d: O won\n", cases);
                continue;
            }
            else if(sum[Tj+4]==-3)
            {
                printf("Case #%d: X won\n", cases);
                continue;
            }
            else if(Ti==Tj)
            {
                if(sum[8]==3)
                {
                    printf("Case #%d: O won\n", cases);
                    continue;
                }
                else if(sum[8]==-3)
                {
                    printf("Case #%d: X won\n", cases);
                    continue;
                }
            }
            else if(Ti+Tj==3)
            {
                if(sum[9]==3)
                {
                    printf("Case #%d: O won\n", cases);
                    continue;
                }
                else if(sum[9]==-3)
                {
                    printf("Case #%d: X won\n", cases);
                    continue;
                }
            }
        for(i=0; i<10; i++)
            if(sum[i]==4)
            {
                printf("Case #%d: O won\n", cases);
                break;
            }
            else if(sum[i]==-4)
            {
                printf("Case #%d: X won\n", cases);
                break;
            }
        if(i==10)
            if(done)
                printf("Case #%d: Draw\n", cases);
            else
                printf("Case #%d: Game has not completed\n", cases);
    }
}
