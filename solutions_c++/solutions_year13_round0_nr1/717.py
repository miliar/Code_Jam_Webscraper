#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>

using namespace std;

#define rep(var,n)  for(int var=0;var<(n);var++)

char board[4][4];

int ts[] = { 0xf000, 0x0f00, 0x00f0, 0x000f,
             0x1111, 0x2222, 0x4444, 0x8888,
             0x8421, 0x1248 };

int check(char c) {
  int m = 0;
  rep(j,4) {
    rep(i,4) {
      m *= 2;
      if (board[j][i] == c || board[j][i] == 'T') ++m;
    }
  }
  rep(i,10){
    if ((m & ts[i]) == ts[i]) return 1;
  }
  return 0;
}

int status(){
  if (check('X')) return 'X';
  if (check('O')) return 'O';

  rep(j,4) rep(i,4) if (board[j][i] == '.') return '-';
  return 'D';
}

main(){
  int _T; cin>>_T;
  rep(_t,_T){
    rep(j,4){
      string s; cin >> s;
      rep(i,4){
        board[j][i] = s[i];
      }
    }
    printf("Case #%d: ", 1+_t);
    switch (status()) {
      case 'X':
        printf("X won\n"); break;
      case 'O':
        printf("O won\n"); break;
      case 'D':
        printf("Draw\n"); break;
      default:
        printf("Game has not completed\n"); break;
    }
  }
}
