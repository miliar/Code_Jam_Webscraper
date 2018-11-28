#include <bits/stdc++.h>

using namespace std;



int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int T, K, i, n, c;
  string S;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cout << "Case #" << t << ": ";
    cin >> S >> K;
    n = S.length();
    c = 0;
    for (i = 0; i < n; ++i) {
      if (S[i] == '+') continue;
      if (i + K > n) break;
      ++c;
      for (int j = i; j < i + K; ++j) {
        S[j] = S[j] == '-' ? '+' : '-';
      }
    }
    if (i == n) {
      cout << c << '\n';
    } else {
      cout << "IMPOSSIBLE\n";
    }
  }
}