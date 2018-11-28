#include <iostream>
#include <vector>
using namespace std;

int main()
{
  int T;
  cin >> T;

  for (int testcase = 1; testcase <= T; ++testcase) {
    int r1;
    vector<vector<int> > c1(4, vector<int>(4));
    cin >> r1;
    --r1;
    for (int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j)
        cin >> c1[i][j];
    }

    int r2;
    vector<vector<int> > c2(4, vector<int>(4));
    cin >> r2;
    --r2;
    for (int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j)
        cin >> c2[i][j];
    }
  
    vector<int> ans;
    for (int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) {
        if (c1[r1][i] == c2[r2][j]) {
          ans.push_back(c1[r1][i]);
        }
      }
    }

    cout << "Case #" << testcase << ": ";
    if (ans.size() == 1) {
      cout << ans[0] << endl;
    } else if (ans.empty()) {
      cout << "Volunteer cheated!" << endl;
    } else {
      cout << "Bad magician!" << endl;
    }
  }
  return 0;
}
