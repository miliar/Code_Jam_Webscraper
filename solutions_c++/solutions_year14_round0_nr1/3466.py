#include <iostream>
#include <cstring>
#include <vector>
using namespace std;

int a[4][4], b[4][4];

int main() {
  int t; cin >> t;
  for (int c = 1; c <= t; c++) {
    int x, y;
    cin >> x;
    for (int i = 0; i < 4; i++)
      for (int j = 0; j < 4; j++)
        cin >> a[i][j];
    cin >> y;
    for (int i = 0; i < 4; i++)
      for (int j = 0; j < 4; j++)
        cin >> b[i][j];

    int ct[32];
    memset(ct, 0, sizeof(ct));
    for (int i = 0; i < 4; i++) {
      ct[a[x-1][i]]++;
      ct[b[y-1][i]]++;
    }

    vector<int> twoct;
    for (int i = 1; i <= 16; i++)
      if (ct[i] == 2)
        twoct.push_back(i);

    cout << "Case #" << c << ": ";
    if (twoct.size() == 1) cout << twoct[0] << endl;
    else if (twoct.size() == 0) cout << "Volunteer cheated!" << endl;
    else cout << "Bad magician!" << endl;
  }
  return 0;
}
