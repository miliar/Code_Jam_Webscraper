#include <bits/stdc++.h>
using namespace std;

vector<int> get_digits(long long num) {
  vector<int> d;
  while (num) {
    d.push_back(num % 10);
    num /= 10;
  }
  return d;
}

long long solve() {
  long long N;
  cin >> N;
  if (N == 0) {
    return -1;
  } else {
    set<int> s;
    long long cnt = 0;
    while (s.size() != 10) {
      ++cnt;
      vector<int> d = get_digits(N * cnt);
      for (int x : d) {
        s.insert(x);
      }
    }
    return N * cnt;
  }
}

int main() {
  ios_base::sync_with_stdio(nullptr);
  cin.tie(nullptr);

  int T;
  cin >> T;
  for (int test = 1; test <= T; ++test) {
    long long value = solve();
    if (value < 0) {
      cout << "Case #" << test << ": INSOMNIA" << endl;
    } else {
      cout << "Case #" << test << ": " << value << endl;
    }
  }
}
