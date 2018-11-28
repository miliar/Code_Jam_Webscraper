#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>

using namespace std;

struct Height {
  int height, row, col;
  
  Height (int h, int i, int j) {
    height = h;
    row = i;
    col = j;
  }

  bool operator< (const Height &a) const {
    if (height < a.height) {
      return true;
    }

    if (height > a.height) {
      return false;
    }

    if (height == a.height) {
      if (row < a.row) {
        return true;
      }

      if (row > a.row) {
        return false;
      }
      
      return col < a.col;
    }

    // NOTE: We should never need this last return
    return false;
  }
};

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {

    //
    // Read the lawn info from standard input
    //
    
    int N, M;
    cin >> N >> M;
    vector<vector<int> > lawn (N, vector<int> (M)); // the lawn configuration
    
    for (int i = 0; i < N; ++i) {
      for (int j = 0; j < M; ++j) {
        cin >> lawn[i][j];
      }
    }
    
    //
    // Verify the lawn configuration
    //

    string result = "YES";
    
    for (int row = 0; row < N; ++row) {
      for (int col = 0; col < M; ++col) {
        int h = lawn[row][col];
        int i, j;
        for (i = 0; (i < N) && (lawn[i][col] <= h); ++i);
        for (j = 0; (j < M) && (lawn[row][j] <= h); ++j);
        if ((i != N) && (j != M)) {
          result = "NO";
          goto output_result;
        }
      }
    }
  output_result:
    cout << "Case #" << t << ": " << result << '\n';
  }
  return 0;
}
