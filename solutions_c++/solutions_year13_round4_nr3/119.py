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
int n;
int d[2010];
bool small[2010][2010];

void regsmall(int p, int q, bool reverse) {
  if (reverse) {
    p = n - 1 - p;
    q = n - 1 - q;
  }
  if (small[p][q]) return;
  small[p][q] = true;
  d[q]++;
  //cerr << p << "<" << q << endl;
}

void process(int a[], bool reverse = false) {
  int lastv[2010];
  mset(lastv, 255);
  lastv[1] = 0;
  int maxv = 1;
  for (int i = 1; i < n; ++i) {
    int v = a[i];
    for (int j = v; j <= maxv; ++j) {
      if (lastv[j] < 0) {
        cerr << "lastv[j] < 0" << endl;
      }
      // x[i] < x[lastv[j]]
      regsmall(i, lastv[j], reverse);
    }
    if (v > 1) {
      // x[lastv[v-1]] < x[i]
      regsmall(lastv[v-1], i, reverse);
    }
    lastv[v] = i;
    if (v > maxv) maxv = v;
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
                fin >> n;
                int a[2010], b[2010];
                for (i = 0; i < n; ++i) {
                  fin >> a[i];
                }
                for (i = 0; i < n; ++i) {
                  fin >> b[n-1-i];
                }
                mset(d, 0);
                mset(small, 0);
                //cerr << "process a" << endl;
                process(a);
                //cerr << "process b" << endl;
                process(b, true);

                int m[2010];
                mset(m, 0);
                for (i = 1; i <= n; ++i) {
                  j = 0;
                  while (j < n && (m[j] || d[j] > 0)) j++;
                  if (j >= n) {
                    cerr << "no sol" << endl;
                    break;
                  }
                  m[j] = i;
                  for (int k = 0; k < n; ++k)
                    if (small[j][k]) {
                      d[k]--;
                    }
                }
		fout << "Case #" << tind << ":";
                for (i = 0; i < n; ++i) fout << ' ' << m[i];
                fout << endl;
	}
	return 0;
}
