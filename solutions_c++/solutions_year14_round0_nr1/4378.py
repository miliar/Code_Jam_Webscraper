#include <iostream>
#include <vector>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int ca = 1; ca <= T; ++ca) {
    vector<bool> can(16, true);
    for (int i = 0; i < 2; ++i) {
      int r;
      cin >> r;
      --r;
      for (int j = 0; j < 4; ++j) {
        for (int k = 0; k < 4; ++k) {
          int x;
          cin >> x;
          if (j != r) {
            can[x-1] = false;
          }
        }
      }
    }
    
    int ans = -1;
    for (int i = 0; i < 16; ++i) if (can[i]) {
      if (ans == -1) ans = i+1;
      else ans = -2;
    }
    
    cout << "Case #" << ca << ": ";
    if (ans == -1) cout << "Volunteer cheated!";
    else if (ans == -2) cout << "Bad magician!";
    else cout << ans;
    cout << endl;
  }
}

