#include<iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <vector>
#include <cmath>
#include <list>
#include <sstream>
#include <algorithm>

using namespace std;

typedef pair<int,int> PII;
typedef long long LL;
typedef vector<int> VI;
typedef pair<LL,LL> PLL;
typedef vector<pair<int,int> > VPII;
typedef vector<LL> VLL;
typedef vector<vector<int> > VVI;
typedef vector<string> VS;
typedef long double LD;

#define PI 3.14159265358979323
#define EE 2.71828182845
#define EPS 10e-10
#define INF 10000000

inline LL MAX(LL a, LL b){ return a < b ? b : a;}
inline LL MIN(LL a, LL b){ return a < b ? a : b;}

//inline LABS(LL a){}

#define FOR(i,n)      for(int i=0;i<(n);i++)
#define FORD(i,n)     for(int i=(n)-1;i>=0;i--)

#define MP make_pair
#define PB push_back

int sol[55][55];
int bol[55][55];

int dx[8] = {-1,-1,-1,0,0,1,1,1};
int dy[8] = {-1,0,1,-1,1,-1,0,1};

bool nula(int x, int y, int R, int C){
  if (sol[x][y] == 1) return false;
  FOR(i,8){
    int tx = x + dx[i];
    int ty = y + dy[i];
    if (tx < 0 || ty < 0 || tx >= R || ty >= C) continue;
    if (sol[tx][ty] == 1) return false;
  }
  return true;
}

int bfs(int odx, int ody, int R, int C){
  queue<int> Q;
  Q.push(odx);
  Q.push(ody);
  memset(bol, 0, sizeof(bol));
  int vratim = 0;
  while(!Q.empty()){
    int wx = Q.front();
    Q.pop();
    int wy = Q.front();
    Q.pop();
    if (bol[wx][wy] != 0) continue;
    bol[wx][wy] = 1;
    vratim++;
    if (nula(wx, wy, R, C) == false) continue;
    for(int i = -1; i <= 1; i++) for (int j = -1; j <= 1; j++) if (j != 0 || i != 0){
      int tx = wx + i;
      int ty = wy + j;
      if (tx < 0 || ty < 0 || tx >= R || ty >= C) continue;
      Q.push(tx); Q.push(ty);
    }
  }
  return vratim;
}

void out(int wx, int wy, int R, int C, int tc){
  cout << "Case #" << tc << ":" << endl;
  FOR(ii, R){
    FOR(jj, C){
      if (wx == ii && wy == jj) cout << "c";
      else if (sol[ii][jj] == 0) cout << "."; else cout << "*";
    }
    cout << endl;
  }
}

void solve(int tc){
  int R, C, M;
  cin >> R >> C >> M;

  int P[R*C];
  FOR(i, R*C) if (i < M) P[i] = 1; else P[i] = 0;
  reverse(P, P+R*C);
  memset(sol, 0, sizeof(sol));

  do{

    //
//    FOR(i, R*C) cout << P[i] << " ";
//    cout << endl;
    //

    FOR(i, R*C) sol[i/C][i%C] = P[i];
/*
    FOR(i, R){
      FOR(j, C){
         cout << sol[i][j] << " ";
      } 
      cout <<endl;
    }
*/

    FOR(i, R) FOR(j, C)if (nula(i,j,R,C)){


      int p = bfs(i,j,R,C);
      if (p + M == R*C){
        out(i,j,R,C, tc);
        return;
      }
    }else if (R*C - M == 1 && sol[i][j] == 0){
        out(i,j,R,C, tc);
        return;
      }


  }while(next_permutation(P, P + R*C));

  cout << "Case #" << tc << ":" << endl << "Impossible" << endl;  
}

int main(){
  int TT;
  cin >> TT;
  FOR(tc, TT) solve(tc + 1);
  return 0;
}
