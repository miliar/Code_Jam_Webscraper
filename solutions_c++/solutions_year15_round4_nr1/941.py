#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
using namespace std;
typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
#define DBG(x) cout << ">>> " << #x << " : " << x << endl
#define PB push_back
#define REP(i,b) for ( int i = 0; i < (b); ++i )
#define FOR(i,a,b) for ( int i = (a); i <= (b); ++i )
#define FORD(i,a,b) for ( int i = (a); i >= (b); --i )
#define RI(a) scanf( "%d", &a )
#define RII(a,b) scanf( "%d%d", &a, &b )
#define RIII(a,b,c) scanf( "%d%d%d", &a, &b, &c )
#define RIIII(a,b,c,d) scanf( "%d%d%d%d", &a, &b, &c, &d )
#define DRI(a) int a; RI(a)
#define DRII(a,b) int a, b; RII(a,b)
#define DRIII(a,b,c) int a, b, c; RIII(a,b,c)
#define DRIIII(a,b,c,d) int a, b, c, d; RIIII(a,b,c,d)
const int INF = 1e9+7;

enum { UP, DOWN, LEFT, RIGHT };
char dir[] = "^v<>";
int neigh[][2] = {
  { -1, 0 },
  { +1, 0 },
  { 0, -1 },
  { 0, +1 }
};
vector<string> board;
map<ii,int>    ids;
int            adj[10005][5];

int d( char c ) {
  REP( i, 4 )
    if ( dir[i] == c )
      return i;
  return -1;
}

int main( ) {
  int caseCnt, rows, cols;

  cin >> caseCnt;
  FOR( caseNr, 1, caseCnt ) {
    memset( adj, 0, sizeof( adj ) );
    int id = 0;
    cin >> rows >> cols;
    cin.get( );
    board.resize( rows );
    REP( r, rows ) {
      getline( cin, board[r] );
    }

    REP( r, rows ) {
      REP( c, cols ) {
        if ( board[r][c] != '.' ) {
          ids[{r,c}] = ++id;
          adj[ids[{r,c}]][4] = d( board[r][c] );
          REP( i, 4 ) {
            for ( int r2 = r + neigh[i][0], c2 = c + neigh[i][1]; r2 >= 0 && r2 < rows && c2 >= 0 && c2 < cols; r2 += neigh[i][0], c2 += neigh[i][1] )
              if ( board[r2][c2] != '.' ) {
                adj[ids[{r,c}]][i] = 1;
                break;
              }
          }
        }
      }
    }

    // FOR( i, 1, id ) {
    //   REP( j, 5 )
    //      cout << adj[i][j] << " ";
    //   cout << endl;
    // }

    int res = 0;
    FOR( i, 1, id ) {
      if ( !adj[i][ adj[i][4] ] ) {
        REP( j, 4 )
          if ( adj[i][j] ) {
            ++res;
            goto next;
          }
        res = -1;
        break;
      }
      next:;
    }
    cout << "Case #" << caseNr << ": ";
    if ( res >= 0 )
      cout << res;
    else
      cout << "IMPOSSIBLE";
    cout << endl;
  }
  return 0;
}