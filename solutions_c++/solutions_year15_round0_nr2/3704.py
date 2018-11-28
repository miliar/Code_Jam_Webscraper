#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>

// time is max pancake size + number of splits
// search for the optimal max pancake size
// for a given max pancake size determining the number of splits is O(N)


using namespace std;

const int MAX_SIZE = 1001;

int main() {
  int T;
  cin >> T;

  for(int tt = 1; tt <= T; tt++) {
    int D;
    vector<int> P;
    cin >> D;
    for(int i = 0; i < D; i++) {
      int temp;
      cin >> temp;
      P.push_back(temp);
    }
    int best_minutes = 2000000000;
    for(int m = 1; m <= MAX_SIZE; m++) {
      int num_splits = 0;
      for(int i = 0; i < P.size(); i++) {
        int pi = P[i];
        int sp = (pi + m - 1)/m - 1;
        num_splits += sp;
      }
      best_minutes = min(num_splits + m, best_minutes);
    }

    cout << "Case #" << tt << ": " << best_minutes << endl;

  }

  return 0;
}
