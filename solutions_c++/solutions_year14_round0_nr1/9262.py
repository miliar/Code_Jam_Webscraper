#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char *argv[])
{
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i) {
    vector< vector<int> > table(4, vector<int>(4, 0));
    int r;
    cin >> r;
    for (int j = 0; j < 4; ++j) {
      for (int k = 0; k < 4; ++k) {
        int v;
        cin >> v;
        table[j][k] = v;
      }
    }

    vector< vector<int> > table2(4, vector<int>(4, 0));
    int r2;
    cin >> r2;
    for (int j = 0; j < 4; ++j) {
      for (int k = 0; k < 4; ++k) {
        int v;
        cin >> v;
        table2[j][k] = v;
      }
    }

    vector<int> result;
    for (int j = 0; j < 4; ++j) {
      if (find(table2[r2 - 1].begin(), table2[r2 - 1].end(), table[r - 1][j]) != table2[r2 - 1].end()) {
        result.push_back(table[r - 1][j]);
      }
    }

    if (result.size() == 1) {
      cout << "Case #" << i + 1 << ": " << result.front() << endl;
    } else if (result.size() == 0) {
      cout << "Case #" << i + 1 << ": Volunteer cheated!" << endl;
    } else {
      cout << "Case #" << i + 1 << ": Bad magician!" << endl;
    }
  }
  return 0;
}
