#include <bits/stdc++.h>
using namespace std;

inline char change(char c) {
  return c == '-' ? '+' : '-';
}

int T;
string S;
int K;

string solve() {
  cin >> S >> K;
  int res = 0;
  for (int i = 0; i + K <= S.size(); ++i) {
    if (S[i] == '+') {
      continue;
    }
    ++res;
    for (int j = 0; j < K; ++j) {
      S[i + j] = change(S[i + j]);
    }
  }
  bool flag = true;
  for (int i = 0; i < S.size(); ++i) {
    if (S[i] == '-') {
      flag = false;
      break;
    }
  }
  return flag ? to_string(res) : "IMPOSSIBLE";
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  cin >> T;
  for (int test = 1; test <= T; ++test) {
    cout << "Case #" << test << ": " << solve() << endl;
  }
}
