#include <cmath>
#include <vector>
#include <fstream>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
  ifstream cin("B-large.in");
  ofstream cout("B.out");

  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int D;
    cin >> D;
    vector<int> P(D);
    for (int i = 0; i < D; i++)
      cin >> P[i];
    int mn = 1e9;
    for (int i = 1; i <= 1000; i++) {
      int minutes = i;
      for (int j = 0; j < D; j++) {
        if (P[j] > i) {
          minutes += ceil((P[j] + 0.0) / i) - 1;
        }
      }
      mn = min(mn, minutes);
    }
    cout << "Case #" << t << ": " << mn << endl;
  }
  return 0;
}
