#include<cstdio>
#include<iostream>
#include<vector>
#include<queue>
#include<set>
#include<map>
#include<string>
#include<sstream>
#include<cmath>
#include<algorithm>


#define FOR(i,a,b) for(int i=int(a);i<int(b);i++)
#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();it++)
#define SQ(x) (x)*(x)

#define BOARD_SIZE 4

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;

int n, xcount, ocount;
char board[BOARD_SIZE][BOARD_SIZE];
bool tpresent;

bool finished(){
  FOR(i,0,BOARD_SIZE){
    FOR(j,0,BOARD_SIZE){
      if(board[i][j]=='.') return false;
    }
  }
  return true;
}

int solve(){
  FOR(i,0,BOARD_SIZE){
    tpresent = false;
    xcount = 0;
    ocount = 0;

    FOR(j,0,BOARD_SIZE){
      if(board[i][j]=='X') xcount++;
      if(board[i][j]=='O') ocount++;
      if(board[i][j]=='T') tpresent = true;
    }

    if(xcount == BOARD_SIZE) return 1;
    if(ocount == BOARD_SIZE) return -1;

    if(tpresent){
      if(xcount == BOARD_SIZE-1) return 1;
      if(ocount == BOARD_SIZE-1) return -1;
    }
  }

  FOR(j,0,BOARD_SIZE){
    tpresent = false;
    xcount = 0;
    ocount = 0;

    FOR(i,0,BOARD_SIZE){
      if(board[i][j]=='X') xcount++;
      if(board[i][j]=='O') ocount++;
      if(board[i][j]=='T') tpresent = true;
    }

    if(xcount == BOARD_SIZE) return 1;
    if(ocount == BOARD_SIZE) return -1;

    if(tpresent){
      if(xcount == BOARD_SIZE-1) return 1;
      if(ocount == BOARD_SIZE-1) return -1;
    }
  }

  // major diag
  tpresent = false;
  xcount = 0;
  ocount = 0;
  FOR(i,0,BOARD_SIZE){
    if(board[i][i]=='X') xcount++;
    if(board[i][i]=='O') ocount++;
    if(board[i][i]=='T') tpresent = true;
  }
  if(xcount == BOARD_SIZE) return 1;
  if(ocount == BOARD_SIZE) return -1;

  if(tpresent){
    if(xcount == BOARD_SIZE-1) return 1;
    if(ocount == BOARD_SIZE-1) return -1;
  }

  // minor diag
  tpresent = false;
  xcount = 0;
  ocount = 0;
  FOR(i,0,BOARD_SIZE){
    if(board[i][BOARD_SIZE-1-i]=='X') xcount++;
    if(board[i][BOARD_SIZE-1-i]=='O') ocount++;
    if(board[i][BOARD_SIZE-1-i]=='T') tpresent = true;
  }
  if(xcount == BOARD_SIZE) return 1;
  if(ocount == BOARD_SIZE) return -1;

  if(tpresent){
    if(xcount == BOARD_SIZE-1) return 1;
    if(ocount == BOARD_SIZE-1) return -1;
  }

  return 0;
}

int main(){
  scanf("%d",&n);
  FOR(ccase,1,n+1){
    FOR(i,0,BOARD_SIZE)
      scanf("%s",board[i]);

    int ans = solve();
    if(ans > 0){
      printf("Case #%d: X won\n",ccase);
    }else if(ans < 0){
      printf("Case #%d: O won\n",ccase);
    }else if(finished()){
      printf("Case #%d: Draw\n",ccase);
    }else{
      printf("Case #%d: Game has not completed\n",ccase);
    }
  }
  return 0;
}
