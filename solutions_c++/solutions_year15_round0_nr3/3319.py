#include <iostream>
#include <string>
#include <vector>
using namespace std;

//                 1  i  j  k -1 -i -j -k
int prod[8][8] = {{0, 1, 2, 3, 4, 5, 6, 7},
                  {1, 4, 3, 6, 5, 0, 7, 2},
                  {2, 7, 4, 1, 6, 3, 0, 5},
                  {3, 2, 5, 4, 7, 6, 1, 0},
                  {4, 5, 6, 7, 0, 1, 2, 3},
                  {5, 0, 7, 2, 1, 4, 3, 6},
                  {6, 3, 0, 5, 2, 7, 4, 1},
                  {7, 6, 1, 0, 3, 2, 5, 4}};

int inv[8] = {0, 5, 6, 7, 4, 1, 2, 3};

int main() {
  int T;
  cin >> T;
  for (int cas = 1; cas <= T; ++ cas) {
    int L, X;
    string word;
    cin >> L >> X >> word;
    bool sol = false;
    int acc = 0;
    int objective = 1;
    for (int i = 0; i < X; ++i) {
      for (int j = 0; j < L; ++j) {
        acc = prod[acc][word[j]-'i'+1];
        if (objective <= 3 and acc == objective) {
          ++objective;
          acc = 0;
        }
      }
    }
    if (objective > 3 and acc == 0) sol = true;
    cout << "Case #" << cas << ": " << (sol? "YES" : "NO") << endl;
  }
}
