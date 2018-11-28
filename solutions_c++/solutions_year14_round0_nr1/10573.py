#include<iostream>
#include<cstdio>
#include<vector>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<map>
#include<cstring>

using namespace std;

typedef long long LL;

	
int main()
{
    int testcases;
    scanf("%d",&testcases);
    for(int k=1;k<=testcases;k++)
    {
      int grid1[5][5],grid2[5][5],row1,row2;
      int count=0,save;
      scanf("%d",&row1);
      for(int i=1;i<=4;i++)
      {
          for(int j=1;j<=4;j++)
          {
              scanf("%d",&grid1[i][j]);
          }
      }
      scanf("%d",&row2);

      for(int i=1;i<=4;i++)
      {
          for(int j=1;j<=4;j++)
          {
              scanf("%d",&grid2[i][j]);
          }
      }

      for(int j=1;j<=4;j++)
      {
        for(int k=1;k<=4;k++)
        {
            if(grid1[row1][j]==grid2[row2][k])
            {
                count++;
                save=grid1[row1][j];
            }
        }
      }
        
      if(count == 0)
        printf("Case #%d: Volunteer cheated!\n",k);
      else if(count == 1)
        printf("Case #%d: %d\n",k,save);
      else if(count > 1)
        printf("Case #%d: Bad magician!\n",k);  
    }
    return 0;
}
