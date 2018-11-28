#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void solve_case(int case_idx) {
  int r0;
  cin >> r0;
  vector<int> row0;
  for (int i = 1; i <= 4; ++i) {
    for (int j = 0; j < 4; ++j) {
      int x;
      cin >> x;
      if (i == r0) {
        row0.push_back(x);
      }
    }
  }

  int r1;
  cin >> r1;
  vector<int> row1;
  for (int i = 1; i <= 4; ++i) {
    for (int j = 0; j < 4; ++j) {
      int x;
      cin >> x;
      if (i == r1) {
        row1.push_back(x);
      }
    }
  }

  sort(row0.begin(), row0.end());
  sort(row1.begin(), row1.end());

  vector<int> choices(4);
  auto it = set_intersection(row0.begin(), row0.end(),
                             row1.begin(), row1.end(),
                             choices.begin());

  int len = distance(choices.begin(), it);
  cout << "Case #" << case_idx << ": ";
  if (len == 0) {
    cout << "Volunteer cheated!\n";
  } else if (len == 1) {
    cout << choices[0] << endl;
  } else {
    cout << "Bad magician!\n";
  }
}

int main() {
  int tests;
  cin >> tests;
  for (int i = 1; i <= tests; ++i) {
    solve_case(i);
  }
  return 0;
}
