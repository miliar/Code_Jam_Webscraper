#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <tuple>
#include <functional>
#include <unordered_set>
#include <algorithm>

using namespace std;


int solve(string S)
{
  int res[100] = {0};
  int i = 1;
  reverse(S.begin(), S.end());
  for (auto &c : S) {
    if (c == '+') {
      if (res[i - 1] % 2 == 1) {
        res[i] = res[i-1] + 1;
      } else {
        res[i] = res[i-1];
      }
    } else {
      if (res[i - 1] % 2 == 0) {
        res[i] = res[i-1] + 1;
      } else {
        res[i] = res[i-1];
      }
    }
    i++;
  }
  return res[i-1];
}

int main(int argc, char *argv[])
{
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    string S;
    cin >> S;
    int res = solve(S);
    cout << "Case #" << t <<": " << res << endl;
  }
  return 0;
}
