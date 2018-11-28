#include <cstdio>
#include <iostream>
#include <list>
#include <algorithm>

#define FOR(i,a,b) for(int i(a); i <= b; ++i)
#define FORD(i,a,b) for(int i(a); i >= b; --i)
#define REP0(i,n) FOR(i,0,n-1)
#define REP1(i,n) FOR(i,1,n)
#define PU push_back
#define PO pop_back
#define MP make_pair
#define A first
#define B second
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(all(c))
#define SZ(s) (int)((s).size())
#define CL(a) memset((a),0,sizeof(a))
#define MAX(X,Y) X = max((X),(Y))
#define MIN(X,Y) X = min((X),(Y))
#define FORIT(X,Y) for(typeof((Y).begin()) X=(Y).begin(); X!=(Y).end(); ++X)
#define VI vector <int>
#define ll long long
#define PII pair<int,int>
#define PDD pair<double,double>
#define INF 1000000000

using namespace std;

#define MAX_R 51
#define MAX_C 51
int R,C,M,blanks;
char grid[MAX_R][MAX_C];
bool visit[MAX_R][MAX_C];
void print() {
  REP1(i,R) {
    REP1(j,C) {
      printf("%c", grid[i][j]);
    }
    printf("\n");
  }
}
int num(int i, int j) {
  int c = 0;
  if (i>1 && j<C && grid[i-1][j+1]=='*') //NE
    c++;
  if (j<C && grid[i][j+1]=='*') //E
    c++;
  if (i<R && j<C && grid[i+1][j+1]=='*') //SE
    c++;
  if (i<R && grid[i+1][j]=='*') //S
    c++;
  if (i<R && j>1 && grid[i+1][j-1]=='*')
    c++;
//  printf("%d %d, c=%d\n", i, j, c);
  return c;
}
void clr(int i, int j, list< PII > &l) {
  if (i>1 && j<C && grid[i-1][j+1]=='*') //NE
    grid[i-1][j+1]='.',l.PU(MP(i-1,j+1));
  if (j<C && grid[i][j+1]=='*') //E
    grid[i][j+1]='.',l.PU(MP(i,j+1));
  if (i<R && j<C && grid[i+1][j+1]=='*') //SE
    grid[i+1][j+1]='.',l.PU(MP(i+1,j+1));
  if (i<R && grid[i+1][j]=='*') //S
    grid[i+1][j]='.',l.PU(MP(i+1,j));
  if (i<R && j>1 && grid[i+1][j-1]=='*')
    grid[i+1][j-1]='.',l.PU(MP(i+1,j-1));
}
bool re(int blanks) {
//  printf("%d\n", blanks);
//  print();
  if (blanks == 0)
    return true;
  REP1(i,R) {
    REP1(j,C) {
      if (visit[i][j]||grid[i][j]=='*')
        continue;
      visit[i][j] = true;
      bool result = false;
      list< PII > l;
      int n = num(i,j);
      if (blanks-n >= 0) {
        clr(i,j,l);
        result = re(blanks-n);
      }
      if (result==false) {
        FORIT(it,l) {
          grid[it->A][it->B] = '*';
        }
        l.clear();
      } else
        return true;
      visit[i][j] = false;
    }
  }
  return false;
}
int T;
void solve() {
  T++;
  cin >> R >> C >> M;
  REP1(i,R) {
    REP1(j,C) {
      grid[i][j] = '*';
      visit[i][j] = false;
    }
  }
  int blanks = R*C-M-1;
  grid[1][1] = 'c';
  bool result = re(blanks);
  printf("Case #%d:\n", T);
  if (result == false)
    printf("Impossible\n");
  else
    print();
}

int main() {
//  freopen("C.in", "r", stdin);
  int T;
  cin >> T;
  while (T-->0) solve();
}
