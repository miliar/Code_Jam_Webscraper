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
void solve() {
  T++;
  int smax;
  cin >> smax;
  int s[smax+1];
  int ac = 0;
  int n = 0;
  REP0(i,smax+1) {
    scanf("%1d", &s[i]);
    if (ac+n < i)
        n = i-ac;
//    printf("%d %d %d\n", s[i], ac, n);
    ac += s[i];
  }
  printf("Case #%d: ", T);
  cout << n << endl;
}

int main() {
//  freopen("A.in", "r", stdin);
  int T;
  cin >> T;
  while (T-->0) solve();
  return 0;
}
