#include <cstdio>
#include <fstream>
#include <algorithm>
using namespace std;
int table1[16][16],table2[16][16],sol[8];
int main()
{
 freopen("A-small-attempt0 (1).in","r",stdin);
  freopen("A-small-attempt0.out","w",stdout);

    int t,no=1;
    scanf("%d",&t);
    while(t--)
    {
        int ans1,ans2;
        scanf("%d",&ans1);
        for(int i=0; i<4; i++)
            for(int j=0; j<4; j++)
                scanf("%d",&table1[i][j]);
        scanf("%d",&ans2);
        for(int i=0; i<4; i++)
            for(int j=0; j<4; j++)
                scanf("%d",&table2[i][j]);
        int index=0;
        for(int i=0; i<4; i++)sol[index++]=table1[ans1-1][i];
        for(int i=0; i<4; i++)sol[index++]=table2[ans2-1][i];
        sort(sol,sol+8);
        int solution=-1;
        bool printed=false;
        for(int i=1; i<8; i++)
            if(sol[i]==sol[i-1])
            {
                if(solution!=-1)
                {
                    printf("Case #%d: Bad magician!\n",no++);
                    printed=true;
                    break;
                }
                solution=sol[i];
            }
        if(!printed)
        {
            if(solution==-1) printf("Case #%d: Volunteer cheated!\n",no++);
            else printf("Case #%d: %d\n",no++,solution);
        }
    }

    return 0;
}
