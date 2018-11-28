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
char S[1005];
void solve() {
  int sMax;
  scanf("%d %s", &sMax, S);
  
  int currStand = 0;
  int toAdd = 0;
  REP(i, sMax + 1) {
    S[i] -= '0';
    if (S[i] > 0) {
      if (currStand < i) {
        int currAdd = i - currStand;
        toAdd += currAdd;
        currStand += currAdd;
      }
      currStand += S[i];
    }
  }
  printf("Case #%d: %d\n", tc, toAdd);
}

int main() {
  int T;
  scanf("%d", &T);
  for (tc = 1; tc <= T; tc++) solve();
	return 0;
}
