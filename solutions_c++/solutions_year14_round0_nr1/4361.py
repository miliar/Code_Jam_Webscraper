#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

void read(vector<int> &vec) {
  int card;
  for (int i = 0; i < 16; ++i) {
    cin >> card;
    vec.push_back(card);
  }
  return;
}

int main() {
  int T, row1, row2, card;
  cin >> T;
  for (int c = 1; T--; c++) {
    vector<int> arrange1, arrange2;
    cin >> row1;
    read(arrange1);
    cin >> row2;
    read(arrange2);
    int cnt = 0;
    auto iter1 = arrange2.begin() + (row2 - 1) * 4, iter2 = iter1 + 4;
    for (int i = 0; i < 4; ++i) {
      if (find(iter1, iter2, arrange1[(row1 - 1) * 4 + i]) != iter2) {
        ++cnt;
        card = arrange1[(row1 - 1) * 4 + i];
      }
    }
    if (cnt == 1)
      cout << "Case #" << c << ": " << card << endl;
    else if (cnt > 1)
      cout << "Case #" << c << ": " << "Bad magician!" << endl;
    else
      cout << "Case #" << c << ": " << "Volunteer cheated!" << endl;
  }
  return 0;
}
