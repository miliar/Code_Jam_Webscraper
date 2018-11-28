#include <bits/stdc++.h>

using namespace std;

int a[5][5], b[5][5];

int main() {
      freopen ("input.txt", "r", stdin);
      freopen ("output.txt", "w", stdout);


      int T, caseNo = 1;
      cin >> T;

      while (T--) {
            cout << "Case #" << caseNo ++ << ": ";
            int row1;
            cin >> row1;
            row1 --;

            for (int i = 0; i < 4; i++)
                  for (int j = 0; j < 4; j++)
                        cin >> a[i][j];
            int row2;
            cin >> row2;
            row2 --;

            for (int i = 0; i < 4; i++)
                  for (int j = 0; j < 4; j++)
                        cin >> b[i][j];

            vector <int> possible;
            for (int i = 0; i < 4; i++) {
                  int elem = a[row1][i], ok = false;
                  for (int j = 0; j < 4; j++) {
                        if (b[row2][j] == elem) {
                              ok = true;
                              break;
                        }
                  }
                  if (ok)
                        possible.push_back(elem);
            }

            if (possible.size() == 0) cout << "Volunteer cheated!" << endl;
            else if (possible.size() >= 2) cout << "Bad magician!" << endl;
            else cout << possible[0] << endl;
      }

      return 0;
}
