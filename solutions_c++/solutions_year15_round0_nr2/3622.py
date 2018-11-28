#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int time(const vector<int> &P, int max_pancake) {
  int t = 0;
  for(int i = 0; i < P.size() && P[i] > max_pancake; i++) t += (P[i]-1) / max_pancake;
  return max_pancake + t;
}

int main() {
  int T;
  cin >> T;
  for(int t = 1; t <=T; t++) {
    int D;
    cin >> D;
    vector<int> P(D);
    for(int i = 0; i < D; i++) cin >> P[i];
    sort(P.rbegin(), P.rend());
    int best = P[0];
    for(int i = P[0]; i > 0; i--) best = min(best, time(P, i));
    cout << "Case #" << t << ": " << best << endl;
  }

}

