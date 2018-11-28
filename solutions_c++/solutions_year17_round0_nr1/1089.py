#include <bits/stdc++.h>
#define FOR(i, n) for (int i = 0; i < (n); ++i)
#define ROF(i, n) for (int i = (n) - 1; i >= 0; --i)
#define REP(i, n) for (int i = 1; i <= (n); ++i)
#define REP3(i, s, n) for (int i = (s); i <= (n); ++i)
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

int K, N;
char S[1002];

int main() {
  int T;
  cin >> T;
  REP (t, T) {
    cin >> S >> K;
    N = strlen(S);

    FOR (i, N) S[i] = (S[i] == '+');

    int flips = 0;
    FOR (i, N - K + 1) {
      if (!S[i]) {
        ++flips;
        FOR (j, K) S[i + j] ^= 1;
      }
    }

    bool ok = true;
    FOR (i, N) if (!S[i]) ok = false;

    cout << "Case #" << t << ": ";
    if (!ok) cout << "IMPOSSIBLE";
    else cout << flips;
    cout << endl;
  }
  return 0;
}
