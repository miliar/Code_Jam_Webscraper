#include <unordered_map>
#include <unordered_set>
#include <map>
#include <list>
#include <algorithm>
#include <memory>
#include <stack>
#include <vector>
#include <queue>
#include <deque>
#include <limits>
#include <iostream>
#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <stdint.h>
#include <inttypes.h>

using namespace std;

int R, C;
char board[128][128];
int dir[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
char symbol[4] = {'>', 'v', '<', '^'};
bool go(int x, int y, int d){
  while(true){
    x += dir[d][0];
    y += dir[d][1];
    if(!(x < R && x >= 0 && y < C && y >= 0) )break;
    if(board[x][y] != '.')return false;
  }
  return true;
}

int solve(){
 int ans = 0;

for(int i = 0; i < R; i++){
  for(int j = 0; j < C; j++){
    if(board[i][j] != '.'){
      bool flag = false;
      for(int k = 0; k < 4; k++){
        if(!go(i, j, k))flag = true;
      }
      //all empty
      if(!flag)return -1;
    }
  }
}

 for(int i = 0; i < R; i++){
    for(int j = 0; j < C; j++){
      if(board[i][j] != '.'){
        for(int k = 0; k < 4; k++){
          if(board[i][j] != symbol[k])continue;
          //empty
          if(go(i,j,k)){
           ans ++;
          }
        }
      }
    }
  }
  return ans;
}


int main() {
  //freopen("test.in", "r", stdin);
  freopen("A-small-attempt0.in", "r", stdin);
  freopen("test.out", "w", stdout);
  int cas;
  scanf("%d", &cas);
  for(int t = 1; t <= cas; t++){
    scanf("%d %d", &R, &C);
    for(int i = 0; i < R; i++){
      scanf("%s", board[i]);
    }
    int result = solve();
    if(result==-1)
      printf("Case #%d: IMPOSSIBLE\n", t);
    else
      printf("Case #%d: %d\n", t, result);
  }
}

