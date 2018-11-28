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
#include <cstring>
using namespace std;

#define mset(A,B) memset(A,B,sizeof(A));
#define mcpy(A,B) memcpy(A,B,sizeof(B));
typedef long long ll;
typedef long double ld;
typedef vector<int> vint;
//typedef vector<string> vstr;
#define FI(I,L,U) for (int I=L;I<U;I++)
#define sqr(x) ((x)*(x))

const ll mm = 1000000007;

ll f[101][4][8];

void update(ll& dest, ll src) {
  dest = (dest + src) % mm;
}

int main()
{
  int tcase = 0;
  ifstream fin("z.in");
  ofstream fout("z.out");
  fin >> tcase;
  for (int tind = 1; tind <= tcase; tind++) {
    int r, c;
    fin >> r >> c;
    mset(f, 0);
    f[0][2][0] = 1;
    f[0][3][0] = 1;
    for (int i = 1; i <= r; i++) {
      // end 3
      if (i >= 2) {
        for (int z = 0; z < 8; z++)
          update(f[i][3][z], f[i-2][2][z]);
      }
      // end 2
      for (int z = 0; z < 8; z++)
        update(f[i][2][z], f[i-1][3][z]);
      if (i >= 2 && c % 3 == 0) {
        for (int z = 0; z < 8; z++)
          update(f[i][2][z | 1], f[i-2][3][z] * 3);
      }
      if (i >= 2 && c % 6 == 0) {
        for (int z = 0; z < 8; z++)
          update(f[i][2][z | 2], f[i-2][3][z] * 6);
      }
      if (i >= 3 && c % 4 == 0) {
        for (int z = 0; z < 8; z++)
          update(f[i][2][z | 4], f[i-3][3][z] * 4);
      }
    }
    ll norm[8] = {1, 3, 6, 6, 4, 12, 12, 12};
    ll ans = 0;
    for (int e = 2; e <= 3; e++)
      for (int z = 0; z < 8; z++)
        ans = (ans + ((f[r][e][z] * ((mm+1) / norm[z])) % mm)) % mm;
    fout << "Case #" << tind << ": " << ans << endl;
  }
  return 0;
}
