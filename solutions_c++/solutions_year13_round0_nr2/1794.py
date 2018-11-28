#include <iostream>
using namespace std;

int n, m;
int map[101][101];

bool judge(int x, int y) {
  int i;
  bool flagx = true;
  bool flagy = true;
  for (i = 0; i < n; ++i) {
    if (map[i][y] > map[x][y]) {
      flagx = false;
    }
  }
  for (i = 0; i < m; ++i) {
    if (map[x][i] > map[x][y]) {
      flagy = false;
    }
  }
  return flagx || flagy;
}

int main() {
  int i, j, k;
  int cases;
  cin >> cases;

  for (i = 1; i <= cases; ++i) {
    cin >> n >> m;
    bool flag = true;

    for (j = 0; j < n; ++j) {
      for (k = 0; k < m; ++k) {
        cin >> map[j][k];
      }
    }

    for (j = 0; j < n; ++j) {
      for (k = 0; k < m; ++k) {
        if (!judge(j, k)) {
          flag = false;
          goto continue_;
        }
      }
    }
continue_:
    if (flag) {
      cout << "Case #" << i << ": YES" << endl;
    } else {
      cout << "Case #" << i << ": NO" << endl;
    }
  }

  return 0;
}
    
