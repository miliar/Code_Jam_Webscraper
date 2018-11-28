#include <algorithm>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

using namespace std;

string solve(int n, int r, int p, int s) {
  string ans = string(p, 'P') + string(r, 'R') + string(s, 'S');
  do {
    string round = ans;
    while (round.size() > 1) {
      string next;
      for (size_t i = 0; i < round.size() / 2; ++i) {
        if (round[2 * i] == round[2 * i + 1]) {
          goto fail;
        } else {
          char a = round[2 * i];
          char b = round[2 * i + 1];
          next.push_back((a == 'P' and b == 'R') or (a == 'S' and b == 'P')
                         or (a == 'R' and b == 'S')? a: b);
        }
      }
      round = next;
    }
    return ans;
fail:
    continue;
  } while (next_permutation(ans.begin(), ans.end()));
  return "IMPOSSIBLE";
}

int main() {
  int t, n, r, p, s;
  cin >> t;
  for (int case_num = 1; case_num <= t; ++case_num) {
    cin >> n >> r >> p >> s;
    cout << "Case #" << case_num << ": " << solve(n, r, p, s) << endl;
  }
  return 0;
}
