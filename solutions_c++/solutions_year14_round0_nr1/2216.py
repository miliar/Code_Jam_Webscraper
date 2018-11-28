#include <cstdio>

using namespace std;

int grid[5][5];
bool sel[25];

int main()
{
    freopen("a.txt","r",stdin);
    freopen("a_out.txt","w",stdout);
    int tc;
    scanf("%d",&tc);
    for (int a=0; a<tc; a++)
    {
        for (int i=0; i<16; i++)
        {
            sel[i]=false;
        }
        int r;
        scanf("%d",&r);
        for (int i=0; i<4; i++)
        {
            for (int j=0; j<4; j++)
            {
                scanf("%d",&(grid[i][j]));
            }
        }
        for (int j=0; j<4; j++)
        {
            sel[grid[r-1][j]-1]=true;
        }
        scanf("%d",&r);
        for (int i=0; i<4; i++)
        {
            for (int j=0; j<4; j++)
            {
                scanf("%d",&(grid[i][j]));
            }
        }
        int cnt=0,ans=0;
        for (int j=0; j<4; j++)
        {
            if (sel[grid[r-1][j]-1])
            {
               cnt+=1;
               ans=grid[r-1][j];
            }
        }
        if (cnt==0)
        {
           printf("Case #%d: Volunteer cheated!\n",a+1);
        }
        else if (cnt==1)
        {
             printf("Case #%d: %d\n",a+1,ans);
        }
        else
        {
            printf("Case #%d: Bad magician!\n",a+1);
        }
    }
}
