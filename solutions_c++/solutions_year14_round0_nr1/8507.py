#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

unordered_set<int> S;

int main() {
  ios_base::sync_with_stdio(0);
  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    int a; cin >> a;
    for (int i = 1; i <= 4; i++) {
      if (i == a) for (int j = 0; j < 4; j++) { int x; cin >> x; S.insert(x); }
      else for (int j = 0; j < 4; j++) {int x; cin >> x; }
    }
    int b, mutual = -1; cin >> b;
    for (int i = 1; i <= 4; i++) {
      if (i == b) for (int j = 0; j < 4; j++) { int x; cin >> x; if (S.count(x)) {if (mutual==-1) mutual = x; else mutual = -8;} }
      else for (int j = 0; j < 4; j++) {int x; cin >> x; }
    }
    if (mutual == -1) cout << "Case #" << t << ": Volunteer cheated!\n";
    else if (mutual > 0) cout << "Case #" << t << ": " << mutual << "\n";
    else cout << "Case #" << t << ": Bad magician!\n";
    S.clear();
  }
}
