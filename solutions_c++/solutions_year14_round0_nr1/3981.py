#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;

int cards[4][4];

int main() {
  int cases;
  cin >> cases;
  for (int c = 1; c <= cases; ++c) {
    int pick;
    cin >> pick;
    --pick;

    for (int row = 0; row < 4; ++row) {
      for (int col = 0; col < 4; ++col) {
        cin >> cards[row][col];
      }
    }

    unordered_set<int> p;
    for (int idx = 0; idx < 4; ++idx) {
      p.insert(cards[pick][idx]);
    }

    cin >> pick;
    --pick;

    for (int row = 0; row < 4; ++row) {
      for (int col = 0; col < 4; ++col) {
        cin >> cards[row][col];
      }
    }

    vector<int> v;
    for (int idx = 0; idx < 4; ++idx) {
      if (p.count(cards[pick][idx]) > 0) {
        v.emplace_back(cards[pick][idx]);
      }
    }

    cout << "Case #" << c << ": ";
    if (v.size() > 1) {
      cout << "Bad magician!";
    } else if (v.empty()) {
      cout << "Volunteer cheated!";
    } else {
      cout << v[0];
    }
    cout << "\n";
  }

  return 0;
}
