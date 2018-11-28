#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <math.h>

using namespace std;

int main() {
  int T = 0;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    int N;
    cin >> N;
    ++N;
    vector<int> S(N);
    for (int j = 0; j < N; ++j) {
      char c;
      cin >> c;
      S[j] = c - '0';
    }
    int now = 0;
    int res = 0;
    for (int j = 0; j < N; ++j) {
      if (now < j) {
        res += j - now;
        now += j - now;
      }
      now += S[j];
    }
    cout << "Case #" << i << ": ";
    cout << res << endl;
  }
}
