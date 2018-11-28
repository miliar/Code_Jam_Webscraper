#include <iostream>
#include <stdio.h>

using namespace std;

int matrix[4][4],matrix2[4][4];

int main()
{
      freopen("A-small-attempt0.in","r",stdin);
      freopen("out.txt","w",stdout);

      int test,row,row2,count,val;
      int test_count=0;
      int i,j;

      scanf("%d",&test);

      while(test--)
      {
          test_count++;
          scanf("%d",&row);
          for(i=0;i<4;i++)
                for(j=0;j<4;j++)
                     scanf("%d",&matrix[i][j]);
          scanf("%d",&row2);
          for(i=0;i<4;i++)
                for(j=0;j<4;j++)
                     scanf("%d",&matrix2[i][j]);
         count=0;
         val;
         for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                if(matrix[row-1][i]==matrix2[row2-1][j])
                {
                       count++;
                       val=matrix[row-1][i];
                }
        if(count==1)
              printf("Case #%d: %d\n",test_count,val);
        else if(count>1)
              printf("Case #%d: Bad magician!\n",test_count);
        else
              printf("Case #%d: Volunteer cheated!\n",test_count);
      }
      return 0;
}
