#include <cstdlib>
#include <cstdio>
#include <iostream>
using namespace std;


int main()
{

    freopen("A-small-attempt0 (1).in","r",stdin);
    freopen("tt","w",stdout);

    int t;
    int x,y;
    int box1[5][5];
    int box2[5][5];
    int k=0;

    scanf("%d",&t);

    while(t--)
    {
        k++;
        scanf("%d",&x);
        x--;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                scanf("%d",&box1[i][j]);
            }
        }
        scanf("%d",&y);
        y--;

        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                scanf("%d",&box2[i][j]);
            }
        }

        int ans=0;
        int ind;

        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if(box1[x][i]==box2[y][j])
                {
                    ans++;
                    ind=i;
                    break;
                }
            }
        }

        if(ans==0)
        {
            printf("Case #%d: Volunteer cheated!\n",k);
        }
        else if(ans==1)
        {
            printf("Case #%d: %d\n",k,box1[x][ind]);
        }
        else
        {
            printf("Case #%d: Bad magician!\n",k);
        }


    }


}
