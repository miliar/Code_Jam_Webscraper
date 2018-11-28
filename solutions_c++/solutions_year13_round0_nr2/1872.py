#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <cmath>
#include <algorithm>
#include <cstring>

using namespace std;

typedef long long int ll;
typedef unsigned long long int ull;

typedef vector <   int  > vi;
typedef vector <   vi   > vvi;
typedef vector < double > vd;
typedef vector <   vd   > vvd;
typedef vector < string > vs;

#define MAX 105

int mat[MAX][MAX];
int maxRow[MAX];
int maxColumn[MAX];

int main () {
  int n, m, T; cin >> T;
  for (int t = 1; t <= T; t++) {
    memset(maxColumn,0,sizeof(maxColumn));
    memset(maxRow,0,sizeof(maxRow));

    cin >> n >> m;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        cin >> mat[i][j];
        maxRow[i] = max(maxRow[i],mat[i][j]);
        maxColumn[j] = max(maxColumn[j],mat[i][j]);
      }
    }

    bool can = true;

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        if (maxRow[i] > mat[i][j] && maxColumn[j] > mat[i][j]) {
          can = false;
          break;
        }
      }
    }

    cout << "Case #" << t << ": " << (can ? "YES" : "NO") << endl;

  }
  return 0;
}
