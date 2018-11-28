#include <vector>
#include <stdio.h>
#include <iostream>

using std::cin;
using std::vector;

void build_grid(int grid[4][4]){
   for(int i = 0; i< 4; i++){
      for(int j = 0; j< 4; j++){
         cin >> grid[i][j];
      }
   }
}

int main(){
   int cases;
   int first_row;
   int second_row;

   vector<int> poss;

   int grid1[4][4];
   int grid2[4][4];

   cin >> cases;

   for(int i = 0; i < cases; i++){
      cin >> first_row;
      build_grid(grid1);

      cin >> second_row;
      build_grid(grid2);

      for(int j = 0; j < 4; j++){
         for(int k = 0; k <4; k++){
            if(grid1[first_row-1][j] == grid2[second_row-1][k]){
               poss.push_back(grid1[first_row-1][j]);
            }
         }
      }
      if(poss.size() == 0){
         printf("Case #%i: Volunteer cheated!\n", i+1);
      }
      else if(poss.size() == 1){
         printf("Case #%i: %i\n", i+1, poss[0]);
      }
      else{
         printf("Case #%i: Bad magician!\n", i+1);
      }
      poss.clear();
   }
   return 0;
}

