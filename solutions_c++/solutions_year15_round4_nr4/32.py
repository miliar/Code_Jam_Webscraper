#include <cstring>
#include <iostream>
using namespace std;

#define MOD 1000000007

int R, C;
int memo[101][13][2][2];
int doit(int r, int rot, int ok2, int ok3) {
  int& ret = memo[r][rot][ok2][ok3];
  if (ret != -1) return ret;
  if (r == R) return ret = 1;
  ret = 0;
  if (ok2) ret = (ret + doit(r+1, rot, 0, 1)) % MOD;
  if (ok3 && r+2 <= R) ret = (ret + doit(r+2, rot, 1, 0)) % MOD;
  if (ok2 && r+2 <= R && C%3 == 0) {
    if (rot%3 == 0) {
      ret = (ret + 3LL * doit(r+2, rot, 0, 1)) % MOD;
    } else {
      ret = (ret + doit(r+2, rot*3, 0, 1)) % MOD;
    }
  }
  if (ok2 && r+2 <= R && C%6 == 0) {
    if (rot%6 == 0) {
      ret = (ret + 6LL * doit(r+2, rot, 0, 1)) % MOD;
    } else if (rot%3 == 0) {
      ret = (ret + 3LL * doit(r+2, rot*2, 0, 1)) % MOD;
    } else if (rot%2 == 0) {
      ret = (ret + 2LL * doit(r+2, rot*3, 0, 1)) % MOD;
    } else {
      ret = (ret + doit(r+2, rot*6, 0, 1)) % MOD;
    }
  }
  if (ok2 && r+3 <= R && C%4 == 0) {
    if (rot%4 == 0) {
      ret = (ret + 4LL * doit(r+3, rot, 0, 1)) % MOD;
    } else if (rot%2 == 0) {
      ret = (ret + 2LL * doit(r+3, rot*2, 0, 1)) % MOD;
    } else {
      ret = (ret + doit(r+3, rot*4, 0, 1)) % MOD;
    }
  }
  return ret;
}

main() {
  int T, prob=1;
  for (cin >> T; T--;) {
    cin >> R >> C;
    memset(memo, -1, sizeof(memo));
    cout << "Case #" << prob++ << ": " << doit(0, 1, 1, 1) << endl;
  }
}
