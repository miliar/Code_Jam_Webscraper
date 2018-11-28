#include <cstdio>

int main()
{
   int nbT;
   scanf("%d", &nbT);
   for(int test=0; test<nbT; test++)
   {
      int row1, grid1[4][4];
      int row2, grid2[4][4];
      scanf("%d", &row1);
      for(int i=0; i<4; i++)
         for(int j=0; j<4; j++)
            scanf("%d", &grid1[i][j]);
      scanf("%d", &row2);
      for(int i=0; i<4; i++)
         for(int j=0; j<4; j++)
            scanf("%d", &grid2[i][j]);
      int r = -1;
      int k = 0;
      for(int i=0; i<4; i++)
         for(int j=0; j<4; j++)
            if(grid1[row1-1][i] == grid2[row2-1][j])
            {
               k++;
               r = grid1[row1-1][i];
            }
      printf("Case #%d: ", test+1);
      if(k == 0) printf("Volunteer cheated!\n");
      else if(k >= 2) printf("Bad magician!\n");
      else printf("%d\n", r);
   }
   return 0;
}
