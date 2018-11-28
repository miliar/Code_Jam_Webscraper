#include <stdio.h>
int first[5][5];
int sec[5][5];
int ans1,ans2;
int my_ans;
int find_intersection();

int main()
{
    freopen("A-small-attempt10.in","r",stdin);
    freopen("c.out","w",stdout);
    int cases;
    scanf("%d",&cases);
    int help;
    int p=1;
    while(cases--)
    {
        scanf("%d",&ans1);
        for(int i=0; i<4; i++)
            for(int j=0; j<4; j++)
                scanf("%d",&first[i][j]);

        scanf("%d",&ans2);
        for(int i=0; i<4; i++)
            for(int j=0; j<4; j++)
                scanf("%d",&sec[i][j]);

        printf("Case #%d: ",p);
        ans1--;
        ans2--;
        help=find_intersection();

        if(help==1)
            printf("%d",my_ans);
        else if(help==0)
            printf("Volunteer cheated!");
        else
            printf("Bad magician!");

        printf("\n");
        p++;

    }
    return 0;
}

int find_intersection()
{
    int inter=0;
    for(int i=0; i<4; i++)
        for(int j=0; j<4; j++)
        {
            if(ans1>=0 && ans2>=0 )
            if(first[ans1][i]==sec[ans2][j])
            {
                inter++;
                my_ans=first[ans1][i];
            }
        }
    return inter;
}

