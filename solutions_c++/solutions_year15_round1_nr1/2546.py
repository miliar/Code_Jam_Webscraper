#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
const double PI = acos(-1);
const double EPS = 1e-7;

#define PB push_back
#define MP make_pair
#define FOR(_i, _from, _to) for (int (_i) = (_from), (_batas) = (_to); (_i) <= (_batas); (_i)++)
#define REP(_i, _n) for (int (_i) = 0, (_batas) = (_n); (_i) < (_batas); (_i)++)
#define SZ(_x) ((int)(_x).size())

int tc;
void solve() {
  int N;
  scanf("%d", &N);
  
  vector<int> data(N);
  REP(i, N) scanf("%d", &data[i]);
  
  // method1
  int ans1 = 0;
  REP(i, N-1) if (data[i] > data[i+1]) ans1 += data[i] - data[i+1];
  
  // method2
  int rate = 0; // rate per 10 mns
  REP(i, N-1) if (data[i] > data[i+1]) rate = max(rate, data[i] - data[i+1]);
  
  int ans2 = 0;
  REP(i, N-1) ans2 += min(rate, data[i]);
  
  printf("Case #%d: %d %d\n", tc, ans1, ans2);
}

int main() {
  int T;
  scanf("%d", &T);
  for (tc = 1; tc <= T; tc++) solve();
	return 0;
}
