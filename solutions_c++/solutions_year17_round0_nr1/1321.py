#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <numeric>

#include <deque>
#include <map>
#include <queue>
#include <stack>
#include <vector>

using namespace std;

typedef long long lint;

#define range(i, a, b, step)                                                   \
  for (int i = (a); i != (int)(b) && ((i - (int)(b)) ^ (int)(step)) < 0;       \
       i += (int)(step))
#define cache(i, a, b, step)                                                   \
  for (int i = (a), i##b = (int)(b), i##step = (int)(step);                    \
       i != i##b && ((i - i##b) ^ i##step) < 0; i += i##step)

int n, t;
string s;

int main(int argc, char const *argv[]) {
#ifndef ONLINE_JUDGE
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
#endif
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  cin >> t;
  range(tcase, 1, t + 1, 1) {
    cin >> s >> n;
    int ans = 0;
    range(i, 0, s.length() - n + 1, 1) {
      if (s[i] == '-') {
        ans += 1;
        range(j, i, i + n, 1) {
          if (s[j] == '-')
            s[j] = '+';
          else
            s[j] = '-';
        }
      }
      // cout << i << ", " << ans << endl;
    }
    bool solved = true;
    range(i, s.length() - n + 1, s.length(), 1) {
      if (s[i] == '-') {
        solved = false;
        break;
      }
    }
    cout << "Case #" << tcase << ": ";
    if (solved)
      cout << ans << endl;
    else
      cout << "IMPOSSIBLE" << endl;
  }

  return 0;
}