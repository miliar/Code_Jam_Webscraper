#include <bits/stdc++.h>

using namespace std;

template <typename T>
void answer(int test, T answer) {
  cout << "Case #" << test << ": " << answer << endl;
}

void solve(int test) {
  int n;
  cin >> n;

  map<int, int> count;

  for (int i = 0; i < 2 * n - 1; i++) {
    for (int j = 0; j < n; j++) {
      int t;
      cin >> t;
      count[t]++;
    }
  }

  vector<int> missing_list;
  for (auto p: count) {
    if (p.second % 2 == 1) {
      missing_list.push_back(p.first);
    }
  }

  if (missing_list.size() != n) {
    cerr << "Bad list size: " << missing_list.size() << ", n = " << n << endl;
  }

  cout << "Case #" << test << ": ";
  for (int i: missing_list) {
    cout << i << ' ';
  }
  cout << endl;
}

int main() {
  int t;
  cin >> t;

  for (int i = 0; i < t; i++) {
    solve(i + 1);
  }
}
