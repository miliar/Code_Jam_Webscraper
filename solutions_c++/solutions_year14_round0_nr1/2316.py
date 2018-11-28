#include <iostream>
#include <set>

using namespace std;

int t;
int guess, in;

int main() {
  freopen("input", "r", stdin);
  freopen("output", "w", stdout);
  cin >> t;
  for (auto c = 1; c <= t; c++) {
    set <int> solutions;
    int res = 0; // No result
    cin >> guess;
    for (auto i = 1; i <= 4; i++) {
      for (int j = 1; j <= 4; j++) {
        cin >> in;
        if (i == guess) solutions.insert(in);
      }
    }
    cin >> guess;
    for (auto i = 1; i <= 4; i++) {
      for (int j = 1; j <= 4; j++) {
        cin >> in;
        if (i == guess && solutions.find(in) != solutions.end()) {
          if (res != 0) res = -1;
          else res = in;
        }
      }
    }

    cout << "Case #" << c << ": ";
    if (res == -1) cout << "Bad magician!";
    else if (res == 0) cout << "Volunteer cheated!";
    else cout << res;
    cout << endl;
  }
  return 0;
}