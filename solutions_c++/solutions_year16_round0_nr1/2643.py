#include <bits/stdc++.h>

using namespace std;

struct Initializer {
  Initializer() {
    cin.tie(0);
    ios::sync_with_stdio(0);
    cout << fixed << setprecision(15);
  }
} initializer;

string solve() {
  int n;
  cin >> n;
  if (n == 0) return "INSOMNIA";
  set<char> used;
  for (int i = 1; ; ++i) {
    for (char c : to_string(n * i)) used.insert(c);
    if (used.size() == 10u) return to_string(n * i);
  }
}

int main() {
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) cout << "Case #" << i << ": " << solve() << endl;
}
