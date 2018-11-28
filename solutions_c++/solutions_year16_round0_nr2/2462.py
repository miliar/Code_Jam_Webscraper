#include <bits/stdc++.h>

using namespace std;

template <typename T>
void answer(int caseNum, T answer) {
  cout << "Case #" << caseNum << ": " << answer << endl;
}

void solve(int caseNum)  {
  string s;
  cin >> s;

  int ans = 0;

  for (int i = 1; i < s.length(); i++) {
    if (s[i] != s[i - 1]) {
      ans++;
    }
  }

  if (s[s.length() - 1] == '-') {
    ans++;
  }

  answer(caseNum, ans);
}

int main() {
  int t;
  cin >> t;

  for (int i = 0; i < t; i++) {
    solve(i + 1);
  }
}
