#include <iostream>
#include <vector>
using namespace std;
int main() {
   int T;
   cin >> T;
   for (int caseN = 1; caseN <= T; caseN++) {
      int N, M;
      cin >> N >> M;
      vector<vector<int> > field;
      vector<int> maxRow;
      vector<int> maxCol;
      maxRow.resize(N);
      maxCol.resize(M);
      field.resize(N);
      for (int i=0; i<N; i++) {
         field[i].resize(M);
         for (int j=0; j<M; j++) {
            cin >> field[i][j];
            maxRow[i] = max(maxRow[i], field[i][j]);
            maxCol[j] = max(maxCol[j], field[i][j]);
         }
      }
      bool ok = true;
      for (int i=0; i<N; i++) {
         for (int j=0; j<M; j++) {
            if (field[i][j] < maxRow[i] && field[i][j] < maxCol[j])
               ok = false;
         }
      }

      cout << "Case #" << caseN << ": ";
      if (ok) {
         cout << "YES";
      } else {
         cout << "NO";
      }
      cout << endl;
   }
}
