#include <algorithm>
#include <cmath>
#include <cstring>
#include <fstream>
#include <iostream>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <cstdlib>
#include <set>
#define DEBUG printf("TEST\n")

using namespace std;

int R, C, itc, TC, ir, ic, i, j, data[105][105];
bool fail;

bool row(int r, int c){
   for(int i = 1; i <= C; ++i)
      if(data[r][i] > data[r][c]) return false;
   return true;
}

bool col(int r, int c){
   for(int i = 1; i <= R; ++i)
      if(data[i][c] > data[r][c]) return false;
   return true;
}

int main(){
   
   scanf("%d", &TC);
   for(itc = 1; itc <= TC; ++itc){
      scanf("%d %d", &R, &C);
      
      for(ir = 1; ir <= R; ++ir){
         for(ic = 1; ic <= C; ++ic) scanf("%d", &data[ir][ic]);
      }
      
      fail = false;
      for(ir = 1; ir <= R && !fail; ++ir){
         for(ic = 1; ic <= C && !fail; ++ic)
            if(!row(ir, ic) && !col(ir, ic)) fail = true;
      }
      
      printf("Case #%d: %s\n", itc, (!fail ? "YES" : "NO"));
   }
   
   return 0;
}
