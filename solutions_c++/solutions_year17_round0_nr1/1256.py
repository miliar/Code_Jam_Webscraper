#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<utility>
#include<iomanip>

using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout << fixed << setprecision(12);

  int64_t T;
  cin >> T;

  for (int64_t t = 1; t <= T; ++t) {
    cout << "Case #" << t << ": ";
    string s;
    cin >> s;
    int64_t k;
    cin >> k;
    int64_t cnt = 0;
    for (int64_t i = 0; i < s.size()-k+1; ++i) {
      if (s[i] == '-') {
        cnt++;
        for (int64_t j = i; j < i + k; ++j) {
          if (s[j] == '-') s[j] = '+';
          else s[j] = '-';
        }
      }
    }
    bool fail = false;
    for (int64_t i = 0; i < s.size(); ++i) {
      if (s[i] == '-') {
        fail = true;
        break;
      }
    }
    if (fail) {
      cout << "IMPOSSIBLE\n";
    } else {
      cout << cnt << '\n';
    }
  }
  return 0;
}

