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

int a[100][100];
int n, m;

bool solve() {
  bool row[100], col[100];
  mset(row, 0);
  mset(col, 0);
  int i, j;
  while (1) {
    int mini = -1, minj, minv = 101;
    for (i = 0; i < n; ++i)
      if (!row[i])
        for (j = 0; j < m; ++j)
          if (!col[j]) {
            if (a[i][j] < minv) {
              minv = a[i][j];
              mini = i;
              minj = j;
            }
          }
    if (minv == 101) {
      return true;
    }
    i = 0;
    while (i < n && (row[i] || a[i][minj] == minv)) i++;
    if (i >= n) {
      col[minj] = true;
      continue;
    }
    j = 0;
    while (j < m && (col[j] || a[mini][j] == minv)) j++;
    if (j >= m) {
      row[mini] = true;
      continue;
    }
    return false;
  }
}

int main()
{
	int tcase = 0;
	ifstream fin("z.in");
	ofstream fout("z.out");
	fin >> tcase;
	for (int tind = 1; tind <= tcase; tind++)
	{
		int i,j;
                fin >> n >> m;
                for (i = 0; i < n; ++i) for (j = 0; j < m; ++j) fin >> a[i][j];
                if (solve()) {
                  fout << "Case #" << tind << ": YES" << endl;
                } else {
                  fout << "Case #" << tind << ": NO" << endl;
                }
	}
	return 0;
}
