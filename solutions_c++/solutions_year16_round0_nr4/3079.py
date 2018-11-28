#include <bits/stdc++.h>

using namespace std;

long long K, C, S;

void solve() {
  long long levels = 0;
  long long cur = 1;
  while (levels < C) {
    cur *= K;
    levels++;
  }

  long long i = 1;
  while (i <= cur) {
    cout << i << " ";
    i += (cur / K);
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int N; cin >> N;
  for (int i = 0; i < N; i++) {
    cin >> K >> C >> S;
    cout << "Case #" << (i + 1) << ": ";
    solve();
    cout << endl;
  }

  return 0;
}
