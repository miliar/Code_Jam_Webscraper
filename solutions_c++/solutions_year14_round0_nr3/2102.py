#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <limits.h>
#include <string>
#include <string.h>
#include <sstream>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <stack>
#include <queue>

using namespace std;

typedef long long ll;

const int dy[8] = {-1,-1,-1,0,0,1,1,1};
const int dx[8] = {-1,0,1,-1,1,-1,0,1};
const char symbol[5] = {'.','*','c','x','u'};

int field[51][51];
int tmp_field[51][51];
int r, c, m;

typedef pair<int, int> coord;

struct board {
  int board[51][51];
};

void init(){
  for(int y = 0; y < r; y++){
    for(int x = 0; x < c; x++){
      field[y][x] = 3;
    }
  }
}

bool check(){
  for(int y = 0; y < r; y++){
    for(int x = 0; x < c; x++){
      if(field[y][x] == 3) return false;
    }
  }

  return true;
}

bool isInside(int y, int x){
  return (0 <= x && x < c && 0 <= y && y < r);
}

void open(int y, int x){
  int ny, nx;
  field[y][x] = 0;

  for(int i = 0; i < 8; i++){
    ny = y + dy[i];
    nx = x + dx[i];

    if( isInside(ny,nx) && field[ny][nx] == 1 ) return;
  }

  for(int i = 0; i < 8; i++){
    ny = y + dy[i];
    nx = x + dx[i];

    if( isInside(ny,nx) && field[ny][nx] == 3){
      open(ny, nx);
    }
  }
}

int mineCount(int num){
  int cnt = 0;
  int val = r*c;

  for(int i = 0; i < val; i++){
    if( num >> i & 1) cnt++;
  }

  return cnt;
}

void setMine(int num){
  int index = 0;

  for(int y = 0; y < r; y++){
    for(int x = 0; x < c; x++){
      if( num >> index & 1){
        field[y][x] = 1;
      }
      index++;
    }
  }
}

void show(){
  for(int y = 0; y < r; y++){
    for(int x = 0; x < c; x++){
      printf("%c",symbol[field[y][x]]);
    }
    printf("\n");
  }
}

bool solver(){
  init();
  int cnt, val = r*c;
  int limit = 1 << val;

  for(int i = 0; i < limit; i++){
    cnt = mineCount(i);
    if( cnt != m ) continue;
    init();
    setMine(i);

    for(int y = 0; y < r; y++){
      for(int x = 0; x < c; x++){
        if(field[y][x] == 3){
          memcpy( tmp_field, field, sizeof(field) );
          open(y,x);

          if( check() ){
            field[y][x] = 2;
            return true;
          }else{
            memcpy( field, tmp_field, sizeof(tmp_field) );
          }
        }
      }
    }
  }

  return false;
}


int main(){
  int test_case;
  cin >> test_case;

  for(int i = 1; i <= test_case; i++){
    cin >> r >> c >> m;
    printf("Case #%d:\n", i);
    if(solver()){
      show();
    }else{
      printf("Impossible\n");
    }
  }

  return 0;
}
