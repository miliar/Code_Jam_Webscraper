#include <bits/stdc++.h>

using namespace std;

template <typename T>
void answer(int test, T answer) {
  cout << "Case #" << test << ": " << answer << endl;
}

int maxIdx(const string& s, int l, int r) {
  char curMax = 0;
  int curIdx = -1;

  for (int i = r; i >= l; i--) {
    if (s[i] > curMax) {
      curMax = s[i];
      curIdx = i;
    }
  }

  return curIdx;
}

void solve(int test) {
  string s;
  cin >> s;

  string result;

  unordered_set<int> taken;

  int r = s.length() - 1;
  while (r >= 0) {
    int nextIdx = maxIdx(s, 0, r);
    result += s[nextIdx];
    taken.insert(nextIdx);
    r = nextIdx - 1;
  }

  for (int i = 0; i < s.length(); i++) {
    if (taken.find(i) == taken.end()) {
      result += s[i];
    }
  }

  answer(test, result);
}

int main() {
  int t;
  cin >> t;

  for (int i = 0; i < t; i++) {
    solve(i + 1);
  }
}
