#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;
#define MAXN 4

char a[MAXN][MAXN];

int check_empty() {
  for(int i = 0; i < MAXN; ++i)
    for(int j = 0; j < MAXN; ++j)
      if('.' == a[i][j])
        return 1;
  return 0;  
}

char check_row(int x) {
  int has_o = 0, has_x = 0, has_t = 0, has_p = 0;
  for(int i = 0; i < MAXN; ++i) {
    has_o += ('O' == a[x][i]);
    has_x += ('X' == a[x][i]);
    has_t += ('T' == a[x][i]);  
    has_p += ('.' == a[x][i]);
  }  
  
  if(has_o && has_x || has_p)
    return 'T';
  if(has_o)
    return 'O';
  return 'X';
}

char check_col(int x) {
  int has_o = 0, has_x = 0, has_t = 0, has_p = 0;
  for(int i = 0; i < MAXN; ++i) {
    has_o += ('O' == a[i][x]);
    has_x += ('X' == a[i][x]);
    has_t += ('T' == a[i][x]);  
    has_p += ('.' == a[i][x]);
  }  
  
  if(has_o && has_x || has_p)
    return 'T';
  if(has_o)
    return 'O';
  return 'X';
}

char check_diag1() {
  int has_o = 0, has_x = 0, has_t = 0, has_p = 0;
  for(int x = 0, y = 0; x < MAXN; ++x, ++y) {
    has_o += ('O' == a[x][y]);
    has_x += ('X' == a[x][y]);
    has_t += ('T' == a[x][y]);  
    has_p += ('.' == a[x][y]);
  }    
  
  if(has_o && has_x || has_p)
    return 'T';
  if(has_o)
    return 'O';
  return 'X';
}

char check_diag2() {
  int has_o = 0, has_x = 0, has_t = 0, has_p = 0;
  for(int x = 0, y = MAXN-1; x < MAXN; ++x, --y) {
    has_o += ('O' == a[x][y]);
    has_x += ('X' == a[x][y]);
    has_t += ('T' == a[x][y]);  
    has_p += ('.' == a[x][y]);
  }    
  
  if(has_o && has_x || has_p)
    return 'T';
  if(has_o)
    return 'O';
  return 'X';
}

void run() {
  for(int i = 0; i < MAXN; ++i) {
    scanf("%s", a[i]);   
  }
  
  for(int i = 0; i < MAXN; ++i) {
    char c = check_row(i);
    if(c != 'T') {
      printf("%c won\n", c);
      return;  
    }  
  }
  
  for(int i = 0; i < MAXN; ++i) {
    char c = check_col(i);
    if(c != 'T') {
      printf("%c won\n", c);
      return;  
    }  
  }
  char c = check_diag1();
  if(c != 'T') {
    printf("%c won\n", c);
    return;  
  }
  
  c = check_diag2();
  if(c != 'T') {
    printf("%c won\n", c);
    return;  
  }
  
  if(check_empty()) {
    printf("Game has not completed\n");
    return;  
  }
  printf("Draw\n");
}

int main() {
  int T;
  scanf("%d", &T);
  for(int i = 0; i < T; ++i) {
    printf("Case #%d: ", i+1);
    run();
  }
  return 0;  
}
