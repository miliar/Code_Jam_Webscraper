#include <iostream>
#include <algorithm>
#include <set>

using namespace std;

int D;
int Pi[1100];
int Copy[1100];

int solve(int target) {
  int needtime = 1000;
  int usedtime = 0;
  for (int i = 1000; i >= target; i--) {
    needtime = min(needtime, i + usedtime);
    Pi[target] += Pi[i];
    Pi[target] = min(Pi[target], 1000);
    Pi[i - target] += Pi[i];
    Pi[i - target] = min(Pi[i - target], 1000);
    usedtime += Pi[i];
    if (usedtime >= 1000) break;
  }
  return needtime;
}

int main(void) {
  int T;

  cin >> T;
  for (int t = 1; t <= T; t++) {
    cin >> D;
    for (int i = 0; i <= 1000; i++) Pi[i] = 0;
    for (int i = 0; i < D; i++) {
      int P; cin >> P;
      Pi[P]++;
    }
    memcpy(Copy, Pi, sizeof(int) * 1100);
    int ans = 1000;
    for (int i = 1; i <= 1000; i++) {
      ans = min(solve(i), ans);
      memcpy(Pi, Copy, sizeof(int) * 1100);
    }
    cout << "Case #" << t << ": " << ans << endl;
  }

  return 0;
}