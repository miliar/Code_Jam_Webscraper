#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

bool solve(const vector<vector<int> >& lawn)
{
  const int R = lawn.size();
  const int C = lawn[0].size();
  
  // vector<int> cmin(C, 100); // min value on the column
  // vector<int> rmin(R, 100); // min value on the row
  
  // for (int i = 0; i < R; ++i) {
  //   for (int j = 0; j < C; ++j) {
  //     rmin[i] = min(rmin[i], lawn[i][j]);
  //     cmin[j] = min(cmin[j], lawn[i][j]);
  //   }
  // }

  // for (int i = 0; i < R; ++i) cout << " " << rmin[i]; cout << endl;
  // for (int j = 0; j < C; ++j) cout << " " << cmin[j]; cout << endl;
    
  for (int i = 0; i < R; ++i) {
    for (int j = 0; j < C; ++j) {
      // you are inside lawn.
      bool higher_on_row = false;
      bool higher_on_col = false;
      for (int r = 0; r < R; ++r) {
	if (lawn[i][j] < lawn[r][j]) higher_on_row = true;
      }
      for (int c = 0; c < C; ++c) {
	if (lawn[i][j] < lawn[i][c]) higher_on_col = true;
      }
      if (higher_on_col && higher_on_row) return false;
    }
  }
  return true;
}


int main()
{
  int T;
  cin >> T;
  for (int cs = 1; cs <= T; ++cs) {
    int R, C;
    cin >> R >> C;

    vector<vector<int> > lawn(R, vector<int>(C, 0));
    for (int i = 0; i < R; ++i) {
      for (int j = 0; j < C; ++j) {
	cin >> lawn[i][j];
      }
    }

    bool ans = solve(lawn);

    cout << "Case #" << cs << ": ";
    if (!ans) cout << "NO" << endl;
    else      cout << "YES" << endl;
  }

  return 0;
}
