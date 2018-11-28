#include <cstdio>
#include <iostream>

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

int board[4][4] = {{0}};
int X, R, C;

bool X1() {
   return false;
}
bool X2() {
   return (R*C%2!=0);
}
bool X3() {
    return (R==1||C==1||R*C%3!=0);
}
bool X4() {
    return (R*C<12||R*C%4!=0);
}
int T;
void solve()
{
  T++;
  cin >> X >> R >> C;
  bool canWin;
  if (X==1)
    canWin = X1();
  else if (X==2)
    canWin = X2();
  else if (X==3)
    canWin = X3();
  else
    canWin = X4();

//  printf("%d %d %d\n", X, R, C);
  printf("Case #%d: ", T);
  if (canWin)
    cout << "RICHARD" << endl;
  else
    cout << "GABRIEL" << endl;

}

int main()
{
//  freopen("D.in", "r", stdin);
  int T;
  cin >> T;
  while (T-->0) solve();
  return 0;
}
