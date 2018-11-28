#include<cstdio>

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.in.txt","w",stdout);
    int bg[20];
    int a,x,i,j,answermode,answer;
    int T,TT;
    scanf("%d",&TT);
    for (T=1;T<=TT;T++)
    {
        for (i=1;i<=16;i++)
            bg[i] = 0;
        answermode = 0;
        scanf("%d",&a);
        for (i=1;i<=4;i++)
        {
            for (j=0;j<4;j++)
            {
                scanf("%d",&x);
                if (i==a)
                    bg[x] = 1;
            }
        }
        scanf("%d",&a);
        for (i=1;i<=4;i++)
        {
            for (j=0;j<4;j++)
            {
                scanf("%d",&x);
                if (i==a and bg[x]==1)
                {
                    if (answermode==0)
                    {
                        answermode = 1;
                        answer = x;
                    }
                    else if (answermode==1)
                        answermode = 2;
                }
            }
        }
        printf("Case #%d: ",T);
        if (answermode==0)
            printf("Volunteer cheated!");
        else if (answermode==1)
            printf("%d",answer);
        else
            printf("Bad magician!");
        printf("\n");
    }
}
