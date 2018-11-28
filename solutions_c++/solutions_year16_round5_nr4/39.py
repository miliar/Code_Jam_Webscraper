#include <bits/stdc++.h>

using namespace std;

void print_answer(int case_id, const string &answer) {
  cout << "Case #" << case_id << ": " << answer << "\n";
}

void solve(int case_id) {
  int n, l; cin >> n >> l;

  bool flag = false;
  for (int i = 0; i < n; i++) {
    string s; cin >> s;

    if (s.find("0") == string::npos) {
      flag = true;
    }
  }

  string b; cin >> b;

  if (flag) {
    print_answer(case_id, "IMPOSSIBLE");
  } else {
    string a = "";
    string b = "";

    for (int i = 0; i < l; i++) {
      a += "0?";
    }
    for (int i = 1; i < l; i++) {
      b += "1";
    }

    if (l == 1) {
      a = "0";
      b = "0?";
    }

    print_answer(case_id, a + " " + b);
  }
}

int main() {
  int cases; cin >> cases;

  for (int i = 1; i <= cases; i++) {
    solve(i);
  }

  return 0;
}