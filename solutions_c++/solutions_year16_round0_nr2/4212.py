#include <iostream>
#include <string>


using namespace std;

int solve(const string &s) {
  int N = (int)s.size() - 1;
  while (N >= 0 && s[N] == '+') N--;
  int i, ans;
  i = ans = 0;
  while (i <= N) {
    int ch = s[i];
    ans++;
    i++;
    while (i <= N && s[i] == ch) i++;
  }
  return ans;
}


int main() {
  int T;
  cin >> T;
  for (int qq = 1; qq <= T; qq++) {
    cout << "Case #" << qq << ": ";
    string s;
    cin >> s;
    cout << solve(s) << endl;
  }
  return 0;
}
