#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int P, Q, N;
vector<int> H, G;

int memo[101][2001][2];
int doit(int m, int sh, int last) {
  if (sh < 0) return -1000000000;
  if (sh > 2000) sh = 2000;
  int& ret = memo[m][sh][last];
  if (ret >= 0) return ret;
  if (m == N) return ret = 0;
  
  ret = doit(m+1, sh + (H[m]+Q-1)/Q-last, 0);
  ret = max(ret, G[m] + doit(m+1, sh - (H[m]+P-1)/P, last));
  int h = H[m];
  if (last) h -= Q;
  if (h <= 0) return ret;

  int ns = 0, ns2 = (h-1)/Q;
  if (P < Q) {
    for (; !(h%Q > 0 && h%Q <= P); h -= P) {
      ns++;
    }
    if (h <= 0) return ret;
    ns2 = (h-1)/Q;
  }
  ret = max(ret, G[m] + doit(m+1, sh - ns + ns2, 1));
  return ret;
}

main() {
  int T, prob=1;
  for (cin >> T; T--;) {
    cin >> P >> Q >> N;
    H.resize(N); G.resize(N);
    for (int i = 0; i < N; i++) cin >> H[i] >> G[i];

    memset(memo, -1, sizeof(memo));
    cout << "Case #" << prob++ << ": " << doit(0, 0, 0) << endl;
  }
}
