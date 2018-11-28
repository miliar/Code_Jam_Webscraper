#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
//#include <utility>
//#include <set>
//#include <map>
//#include <queue>
#include <iomanip>
using namespace std;

#define mset(A,B) memset(A,B,sizeof(A));
#define mcpy(A,B) memcpy(A,B,sizeof(B));
typedef long long ll;
typedef long double ld;
typedef vector<int> vint;
//typedef vector<string> vstr;
#define FI(I,L,U) for (int I=L;I<U;I++)
#define sqr(x) ((x)*(x))

int r, c;
string m[101];

int solve() {
  int ans = 0;
  for (int i = 0; i < r; i++)
    for (int j = 0; j < c; j++) {
      if (m[i][j] == '.') continue;
      int dx = 0, dy = 0;
      if (m[i][j] == '<') dy = -1;
      if (m[i][j] == '>') dy = 1;
      if (m[i][j] == '^') dx = -1;
      if (m[i][j] == 'v') dx = 1;
      int x = i + dx, y = j + dy;
      bool ok = false;
      while (x >= 0 && x < r && y >= 0 && y < c) {
        if (m[x][y] != '.') {
          ok = true;
          break;
        }
        x += dx; y += dy;
      }
      if (ok) continue;
      ok = false;
      for (int k = 0; k < c; k++) if (k != j && m[i][k] != '.') ok = true;
      for (int k = 0; k < r; k++) if (k != i && m[k][j] != '.') ok = true;
      if (!ok) return -1;
      ans++;
    }
  return ans;
}

int main()
{
  int tcase = 0;
  ifstream fin("z.in");
  ofstream fout("z.out");
  fin >> tcase;
  for (int tind = 1; tind <= tcase; tind++) {
    fin >> r >> c;
    for (int i = 0; i < r; i++) fin >> m[i];
    int ans = solve();
    if (ans < 0)
      fout << "Case #" << tind << ": IMPOSSIBLE" << endl;
    else
      fout << "Case #" << tind << ": " << ans << endl;
  }
  return 0;
}
