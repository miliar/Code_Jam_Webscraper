#include <iostream>
using namespace std;
int cards[16];
int main() {
  int T; cin >> T;
  int ncase = 0;
  while (T--) {
    int row;
    cin >> row; --row;
    for (int i = 0; i < 16; ++i) {
      int k; cin >> k;
      cards[k-1] = (i/4 == row);
    }
    cin >> row; --row;
    int t = 0;
    int card;
    for (int i = 0; i < 16; ++i) {
      int k; cin >> k;
      if (i/4 == row and cards[k-1]) {
        ++t;
        card = k;
      }
    }
    cout << "Case #" << ++ncase << ": ";
    if (!t) cout << "Volunteer cheated!" << endl;
    else if (t == 1) cout << card << endl;
    else cout << "Bad magician!" << endl;
  }
}