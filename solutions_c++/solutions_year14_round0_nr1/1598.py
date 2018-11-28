#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;

void readConfiguration(int grid[4][4]) {
   for(int i = 0; i < 4; ++i)
      for(int j = 0; j < 4; ++j) 
         scanf("%d", &grid[i][j]);
}

int main() {
   int t;
   scanf("%d", &t);

   for(int c = 1; c <= t; ++c) {
      int card = -1;
      int row1, row2;
      int configuration1[4][4],
          configuration2[4][4];

      scanf("%d", &row1);
      readConfiguration(configuration1);
      scanf("%d", &row2);
      readConfiguration(configuration2);

      --row1;
      --row2;

      bool visited[16] = { 0 };

      for(int i = 0; i < 4; ++i)
         visited[configuration1[row1][i] - 1] = true;

      for(int i = 0; i < 4; ++i) {
         int current = configuration2[row2][i];
         if (visited[current - 1]) {
            if (card != -1)
               card = -2;
            else
               card = current;

         }
      }

      if (card > 0)
         printf("Case #%d: %d\n", c, card);
      else if(card == -1)
         printf("Case #%d: Volunteer cheated!\n", c);
      else
         printf("Case #%d: Bad magician!\n", c);
   }
}
