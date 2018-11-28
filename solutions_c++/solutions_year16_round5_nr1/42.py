#include <bits/stdc++.h>

using namespace std;

void print_answer(int case_id, int answer) {
  cout << "Case #" << case_id << ": " << answer << "\n";
}

vector<char> vc;

void solve(int case_id) {
  vc.clear();
  string s; cin >> s;

  int answer = 0;
  for (char c : s) {
    if (vc.size() && vc.back() == c) {
      answer += 10;
      vc.pop_back();
    } else {
      vc.push_back(c);
    }
  }

  answer += 5 * (vc.size() / 2);

  print_answer(case_id, answer);
}

int main() {
  int cases; cin >> cases;

  for (int i = 1; i <= cases; i++) {
    solve(i);
  }

  return 0;
}