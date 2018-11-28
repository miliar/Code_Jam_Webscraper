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

const int MAX_N = 1000;
int tc;
int N;
int data[MAX_N + 5];

void solve() {
  scanf("%d", &N);
  REP(i, N) scanf("%d", &data[i]);
  
  int maxElement = *max_element(data, data + N);
  int ans = maxElement;
  for (int boleh = 1; boleh <= maxElement; boleh++) {
    
    int special = 0;
    REP(i, N) {
      if (data[i] > boleh) {
        int toTransfer = data[i] - boleh;
        int useSpecial = (toTransfer + boleh - 1) / boleh;
        special += useSpecial;
      }
    }
    ans = min(ans, special + boleh);
  }
  
  printf("Case #%d: %d\n", tc, ans);
}

int main() {
  int T;
  scanf("%d", &T);
  for (tc = 1; tc <= T; tc++) solve();
	return 0;
}
