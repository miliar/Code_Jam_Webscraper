#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctime>
#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;

typedef pair<int,int> ii;
typedef long long LL;
typedef vector <int> vi;

#define INF 2000000000
#define PI 3.14159265

#define REP(i,n) for(int i=0, _n=n; i<_n; ++i)
#define FOR(i,a,n) for(int i=a,_n=n; i<=_n; ++i)
#define FOREACH(it,arr) for (__typeof((arr).begin()) it=(arr).begin(); it!=(arr).end(); it++)

#define ALL(v) (v).begin(), (v).end()

#define DEBUG(x) cout << '>' << #x << ':' << x << '\n';

//0 means row
//1 means col
//2 means diagonal
bool isSameVal(char X, int code, char board[][5]) {
   if ( code == 0 ) {
      REP (i, 4) {
         bool isSame = true;
         REP (j, 4) {
            char curr = board[i][j];
            if ( !(curr == X || curr == 'T') ) isSame = false;
         }
         if ( isSame ) return true;
      }
      return false;
   }

   if ( code == 1 ) {
      REP (i, 4) {
         bool isSame = true;
         REP (j, 4) {
            char curr = board[j][i];
            if ( !(curr == X || curr == 'T') ) isSame = false;
         }
         if ( isSame ) return true;
      }
      return false;
   }

   if ( code == 2 ) {
      bool isSame = true;
      REP (i, 4) {
         char curr = board[i][i];
         if ( !(curr == X || curr == 'T') ) isSame = false;
      }
      if ( isSame ) return true;

      isSame = true;
      REP (i, 4) {
         int j = 3-i;
         char curr = board[i][j];
         if ( !(curr == X || curr == 'T') ) isSame = false;
      }
      return isSame;
   }
}

bool isXWon(char board[][5]) {
   if ( isSameVal('X', 0, board) ) return true;
   if ( isSameVal('X', 1, board) ) return true;
   if ( isSameVal('X', 2, board) ) return true;

   return false;
}

bool isOWon(char board[][5]) {
   if ( isSameVal('O', 0, board) ) return true;
   if ( isSameVal('O', 1, board) ) return true;
   if ( isSameVal('O', 2, board) ) return true;

   return false;
}

bool noDot(char board[][5]) {
   bool noDot = true;
   REP (i, 4) {
      REP (j, 4) {
         if ( board[i][j] == '.' ) noDot = false;
      }
   }

   return noDot;
}

int main() {
   freopen("a-large.in", "r", stdin);
   freopen("a-large.out", "w", stdout);
   int t; scanf("%d", &t);

   REP (x, t) {
      char board[4][5];
      REP (i, 4) scanf("%s", board[i]);
      getchar();

      printf("Case #%d: ", x+1);
      if ( isXWon(board) )
         puts("X won");
      else if ( isOWon(board) )
         puts("O won");
      else if ( noDot(board) )
         puts("Draw");
      else
         puts("Game has not completed");

   }

   return 0;
}
