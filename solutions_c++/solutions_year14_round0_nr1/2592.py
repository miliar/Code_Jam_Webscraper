#include <set>
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
  int T;
  cin >> T;

  for (int i = 1; i <= T; ++i) {
    int row1, row2;
    set<int> rows1;
    set<int> rows2;

    cin >> row1;
    for (int k = 0; k < 16; k++) {
      int tmp;
      cin >> tmp;
      if ((k / 4 + 1) == row1) {
        rows1.insert(tmp);
      }
    }

    cin >> row2;
    for (int k = 0; k < 16; k++) {
      int tmp;
      cin >> tmp;
      if ((k / 4 + 1)  == row2) {
        rows2.insert(tmp);
      }
    }

    set<int> rset;
    set_intersection(rows1.begin(), rows1.end(), rows2.begin(), rows2.end(), inserter(rset, rset.begin()));
    cout << "Case #"<<i<< ": ";
    if (rset.size() == 0)
      cout << "Volunteer cheated!" << endl;
    else if (rset.size() > 1)
      cout << "Bad magician!" << endl;
    else
      cout << *rset.begin() << endl;
  }
}
