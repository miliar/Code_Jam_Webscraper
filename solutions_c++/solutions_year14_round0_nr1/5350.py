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
  int a[2], card[2][4][4];
  REP0(k,2) {
    cin >> a[k];
    REP0(i,4) {
      REP0(j,4) {
        cin >> card[k][i][j];
      }
    }
  }
  int cnt[17] = {0};
  REP0(i,4) {
    cnt[card[0][a[0]-1][i]]++;
    cnt[card[1][a[1]-1][i]]++;
  }
  int ans = 0;
  int num_ans = 0;
  REP1(i,16) {
    if (cnt[i] == 2) {
      ans = i;
      num_ans++;
    }
  }
  printf("Case #%d: ", T);
  if (num_ans == 1)
    printf("%d\n", ans);
  else if (num_ans > 1)
    printf("Bad magician!\n");
  else
    printf("Volunteer cheated!\n");
}

int main() {
//  freopen("A.in", "r", stdin);
  int T;
  cin >> T;
  while (T-->0) solve();
}
