#include <iostream>
#include <vector>

using namespace std;


int h, w;
int garden[100][100];

bool rangeCheck(int y, int x){
  if(y < 0 || h-1 < y){
    return false;
  }
  if(x < 0 || w-1 < x){
    return false;
  }
  return true;
}


bool v_check(int y, int x, int value){
  bool flag = true;

  for(int ypos = y; ypos >= 0; ypos--){
    if(rangeCheck(ypos, x) && garden[ypos][x] > value){
      flag = false;
      break;
    }
  }
  
  for(int ypos = y; ypos < h; ypos++){
    if(rangeCheck(ypos, x) && garden[ypos][x] > value){
      flag = false;
      break;
    }
  }

  return flag;
}

bool h_check(int y, int x, int value){
  bool flag = true;

  for(int xpos = x; xpos >= 0; xpos--){
    if(rangeCheck(y, xpos) && garden[y][xpos] > value){
      flag = false;
      break;
    }
  }

  for(int xpos = x; xpos < w; xpos++){
    if(rangeCheck(y, xpos) && garden[y][xpos] > value){
      flag = false;
      break;
    }
  }

  return flag;
}

bool check(int y, int x){
  bool flag1, flag2;
  int value = garden[y][x];
  flag1 = v_check(y, x, value);
  flag2 = h_check(y, x, value);

  if(flag1 || flag2){
    return true;
  }else{
    return false;
  }
}

void solve(int n, int m, int case_num){
  int elem;
  bool flag = true;
  for(int y=0; y<n; y++){
    for(int x=0; x<m; x++){
      cin >> elem;
      garden[y][x] = elem;
    }
  }

  for(int y=0; y<n; y++){
    for(int x=0; x<m; x++){
      flag &= check(y, x);
    }
  }
  if(flag){
    printf("Case #%d: YES\n", case_num);
  }else{
    printf("Case #%d: NO\n", case_num);
  }
}

int main(){
  int t;
  int n, m;
  cin >> t; 

  for(int i=0; i<t; i++){
    cin >> n >> m;
    h = n;
    w = m;
    solve( n, m, i+1 );
  }
  return 0;
}
