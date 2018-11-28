#include <iostream>
using namespace std;

int main ()
{
  int t, h = 1, i, j, v, ctr, c1, c2;
  int a1[4][4], a2[4][4];
  cin >> t;
  while (h <= t) {
    cin >> c1;
    c1--;
    for (i = 0; i < 4; i++)
      for (j = 0; j < 4; j++)
        cin >> a1[i][j];

    cin >> c2;
    c2--;
    for (i = 0; i < 4; i++)
      for (j = 0; j < 4; j++)
        cin >> a2[i][j];

    ctr = 0;
    v = -1;
    for (i = 0; i < 4; i++) {
      for (j = 0; j < 4; j++) {
        if (a1[c1][i] == a2[c2][j]) {
          ctr++;
          v = a1[c1][i];
        }
      }
    }

    cout << "Case #" << h++ << ": ";
    if (ctr == 0)
      cout << "Volunteer cheated!" << endl;
    else if (ctr > 1)
      cout << "Bad magician!" << endl;
    else
      cout << v << endl;
  }

  return 0;
}
