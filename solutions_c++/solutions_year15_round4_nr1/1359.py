#include<bits/stdc++.h>
using namespace std;
#define REP(i,n) for(int i = 0; i < (n); i++)
typedef long long LL;
int scani(){int x; assert(scanf("%d", &x) == 1); return x;}
void scans(char* w){assert(scanf("%s", w) == 1);}

const int RC = 100;
enum direction {UP=0,DOWN=1,LEFT=2,RIGHT=3};
char board[RC][RC+1];
bool is_good[RC][RC][4];
direction char2dir(char c){
  if(c == '^') return UP;
  if(c == 'v') return DOWN;
  if(c == '<') return LEFT;
  if(c == '>') return RIGHT;
  assert(false);
}

direction dir(int i, int j){
  return char2dir(board[i][j]);
}

int count_good(int i, int j){
  return is_good[i][j][0] + is_good[i][j][1]
       + is_good[i][j][2] + is_good[i][j][3];
}
#define DEBUG if(0)
int main(){
  int T = scani();
  REP(t, T){
    int r = scani(), c = scani();
    REP(i, r) REP(j, c) REP(d, 4) is_good[i][j][d] = 1;
    REP(i, r) scans(board[i]);
    REP(i, r){
      int j;
      j = 0;
      while(j < c && board[i][j] == '.') j++;
      if(j < c) {
        is_good[i][j][LEFT] = false;
        DEBUG cout << i << " " << j << " " << "L" << endl;
      }
      j = c;
      while(j-1 >= 0 && board[i][j-1] == '.') j--;
      if(j-1 >= 0){
        is_good[i][j-1][RIGHT] = false;
        DEBUG cout << i << " " << j << " " << "R" << endl;
      }
    }
    REP(j, c){
      int i;
      i = 0;
      while(i < r && board[i][j] == '.') i++;
      if(i < r) {
        is_good[i][j][UP] = false;
        DEBUG cout << i << " " << j << " " << "U" << endl;
      }
      i = r;
      while(i-1 >= 0 && board[i-1][j] == '.') i--;
      if(i-1 >= 0){
        is_good[i-1][j][DOWN] = false;
        DEBUG cout << i << " " << j << " " << "D" << endl;
      }
    }
    bool possible = true;
    int changes = 0;
    REP(i, r)
      REP(j, c){
      if(board[i][j] != '.' && !is_good[i][j][dir(i,j)]){
        if(count_good(i, j) > 0) changes++;
        else possible = false;
      }
    }
    printf("Case #%d: ", t+1);
    if(!possible) printf("IMPOSSIBLE\n");
    else printf("%d\n", changes);
  }
  return 0;
}
