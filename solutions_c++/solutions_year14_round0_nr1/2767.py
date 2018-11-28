#include <algorithm>
#include <iostream>
#include <set>

using namespace std;

int main()
{
  int T;
  cin >> T;
  for (int k = 1; k <= T; ++k) {
    cout << "Case #" << k << ": ";

    set<int> fst;
    set<int> scd;

    int row; cin >> row;
    for (int i = 0; i < 4; ++i)
      for (int j = 0; j < 4; ++j) {
        int x; cin >> x;
        if (i + 1 == row)
          fst.insert(x);
      }
    cin >> row;
    for (int i = 0; i < 4; ++i)
      for (int j = 0; j < 4; ++j) {
        int x; cin >> x;
        if (i + 1 == row)
          scd.insert(x);
      }

    set<int> both;
    set_intersection(fst.begin(), fst.end(),
        scd.begin(), scd.end(),
        inserter(both, both.begin()));

    if (both.size() > 1)
      cout << "Bad magician!\n";
    else if (both.empty())
      cout << "Volunteer cheated!\n";
    else
      cout << *both.begin() << "\n";
  }

  return 0;
}
