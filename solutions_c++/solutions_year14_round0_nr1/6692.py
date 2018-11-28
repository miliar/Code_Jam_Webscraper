#include <iostream>
#include <map>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int CASE = 1; CASE <= T; CASE++) {
    int val, ans;
    map<int, int> cnt;
    for (int i = 0; i < 2; i++) {
      cin >> ans;
      for (int j = 1; j <= 4; j++)
      for (int k = 1; k <= 4; k++) {
        cin >> val;
        if (j == ans)
          cnt[val]++;
      }
    }
    ans = -1;
    int cnt2 = 0;
    for (auto p : cnt) {
      if (p.second == 2) {
        cnt2++;
        ans = p.first;
      }
    }
    cout << "Case #" << CASE << ": ";
    if (cnt2 == 1) {
      cout << ans;
    } else if (cnt2 > 1) {
      cout << "Bad magician!";
    } else {
      cout << "Volunteer cheated!";
    }
    cout << endl;
  }
}