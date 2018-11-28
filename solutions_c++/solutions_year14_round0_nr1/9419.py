#include<cstdio>
#include<cstring>
#include<cmath>

using namespace std;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int cases,follow;
    scanf("%d",&cases);
    for(follow=1; follow<=cases; follow++)
    {
        int first, second;
        int grid[4][4],temp[4];
        scanf("%d",&first);

        for(int i=0; i<4; i++)
            for(int j=0; j<4; j++)
                scanf("%d",&grid[i][j]);

        for(int i=0; i<4; i++ )
        {
            temp[i]=grid[first-1][i];


        }
        scanf("%d",&second);

        for(int i=0; i<4; i++)
            for(int j=0; j<4; j++)
                scanf("%d",&grid[i][j]);
        int number =0,c;

        for(int i=0; i<4; i++)
            for(int j=0; j<4; j++)
            {
                if(temp[i]==grid[second-1][j])
                {

                    c=temp[i];
                    number++;
                }

            }
        if(number==1)
            printf("Case #%d: %d\n",follow,c);
        else if(number>1)
            printf("Case #%d: Bad magician!\n",follow);
        else if(number==0)
            printf("Case #%d: Volunteer cheated!\n",follow);







    }


    return 0;
}
