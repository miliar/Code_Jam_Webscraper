#include <iostream>
#include <string>

using namespace std;

void solve_case(int case_id) {
  int n; cin >> n;
  string s; cin >> s;

  int standing = s[0] - '0';
  int friends = 0;
  for (int i = 1; i <= n; ++i) {
    if (standing < i) {
      friends += i - standing;
      standing = i;
    }
    standing += s[i] - '0';
  }

  cout << "Case #" << case_id << ": " << friends << endl;
}

int main() {
  int t; cin >> t;
  for (int i = 1; i <= t; ++i) {
    solve_case(i);
  }
  return 0;
}
