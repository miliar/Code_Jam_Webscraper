#include <iostream>
using namespace std;

int main() {
  int T; cin >> T;
  for (int x = 1; x <= T; ++x) {
    int a1; cin >> a1;
    int r1[16];
    for(int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) {
        int n; cin >> n;
        r1[n-1] = i+1;
      }
    }
    int a2; cin >> a2;
    int r2[16];
    for(int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) {
        int n; cin >> n;
        r2[n-1] = i+1;
      }
    }
    int result = 0;
    for(int n = 0; n < 16; ++n) {
      if (r1[n] == a1 && r2[n] == a2) {
        if (result == 0) result = n+1;
        else result = -1; // bad magician
      }
    }
    cout << "Case #" << x << ": ";
    if (result == 0) cout << "Volunteer cheated!";
    else if (result == -1) cout << "Bad magician!";
    else cout << result;
    cout << endl;
  }
}
