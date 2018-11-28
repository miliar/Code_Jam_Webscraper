#include <iostream>
#include <algorithm>
#include <set>

using namespace std;

void
solve() {
  set<int> S[2];
  for (int s = 0; s < 2; ++s) {
    int a;
    cin >> a;
    for (int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) {
        int n;
        cin >> n;
        if (i + 1 == a) {
          S[s].insert(n);
        }
      }
    }
  }

  set<int> I;
  set_intersection(S[0].begin(), S[0].end(),
                   S[1].begin(), S[1].end(),
                   inserter(I, I.begin()));

  if (I.size() == 1) {
    cout << *I.begin();
  } else if (I.size() == 0) {
    cout << "Volunteer cheated!";
  } else {
    cout << "Bad magician!";
  }
  cout << endl;
}

int
main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cout << "Case #" << t << ": ";
    solve();
  }
  
  return 0;
}
