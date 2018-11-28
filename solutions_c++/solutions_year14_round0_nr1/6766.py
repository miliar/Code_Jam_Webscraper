#include <iostream>
#include <map>

using namespace std;

int main() {
  int T;
  cin >> T;

  for (int t = 0; t < T; t++) {
    map<int,bool> possible;
    int row1,row2;
    cin >> row1;
    cerr << "Case t:" << t << endl;
    for (int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) {
        int temp;
        cin >> temp;
        cerr << temp  << " ";
        if (i+1==row1) {
          possible[temp] = true;
        }
      }
      cerr << endl;
    }
    cin >> row2;
    int res = -1;
    int n_found = 0;
    for (int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) {
        int temp;
        cin >> temp;
        cerr << temp  << " ";
        if (i+1 == row2 && possible[temp]) {
          ++n_found;
          res = temp;
        }
      }
    }


    cout << "Case #" << t+1 << ": ";
    if (n_found == 0) {
      cout << "Volunteer cheated!";
    } 
    if (n_found == 1) {
      cout << res;
    } 
    if (n_found > 1) {
      cout << "Bad magician!";
    } 
    cout << endl;
  }
  return 0;
}
