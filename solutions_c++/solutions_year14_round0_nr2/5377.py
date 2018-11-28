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

int T;
void solve()
{
  T++;
  double C,F,X,t=0,t0,t1,t2,R=2;
  cin >> C >> F >> X;
  while (1) {
	  t0 = C/R;
	  t1 = t0+X/(R+F); // time if buying a new farm
	  t2 = X/R; // time if not buying a new farm
	  if (t2 < t1) {
		  t += t2;
		  break;
	  }
	  t += t0;
	  R += F;
  }
  printf("Case #%d: %.7f\n", T, t);
}

int main()
{
//  freopen("B.in", "r", stdin);
  int T;
  cin >> T;
  while (T-->0) solve();
}
