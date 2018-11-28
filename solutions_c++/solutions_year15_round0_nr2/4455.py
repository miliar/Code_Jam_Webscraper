#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

const int INF = 1 << 30;

int solve(vector<int> P, int d, const int P_max) {
  if (P[0] <= 3) {
    return P[0];
  }

  if (d >= 9) {
    return INF;
  }

  int ret = P[0];
  for (int i = 1; i < P[0]; ++i) {
    vector<int> _P = P;
    _P[0] -= i;
    _P.push_back(i);
    
    sort(_P.begin(), _P.end(), greater<int>());
    ret = min(ret, solve(_P, d + 1, P_max) + 1);
  }
  return ret;
}

int main() {
  int T;
  cin >> T;
  for (int testcase = 1; testcase <= T; ++testcase) {
    int D;
    cin >> D;

    vector<int> P(D);
    for (int i = 0; i < D; ++i) {
      cin >> P[i];
    }
    sort(P.begin(), P.end(), greater<int>());

    cout << "Case #" << testcase << ": " << solve(P, 0, P[0]) << endl;
  }
  return 0;
}
