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

string s;

int convert(char ch) {
  if (ch == 'i') return 2;
  if (ch == 'j') return 3;
  if (ch == 'k') return 4;
  cerr << "invalid char " << ch << endl;
  return 1;
}

static const int table[4][4] = {
  {1, 2, 3, 4},
  {2, -1, 4, -3},
  {3, -4, -1, 2},
  {4, 3, -2, -1},
};

int mul(int a, int b) {
  int res = 1;
  if (a < 0) {
    res = -res;
    a = -a;
  }
  if (b < 0) {
    res = -res;
    b = -b;
  }
  res *= table[a - 1][b - 1];
  return res;
}

bool check(int n, long long x) {
  int z = 1;
  for (int i = 0; i < n; i++) {
    z = mul(z, convert(s[i]));
  }
  if (z == 1) return false;
  if (z == -1) {
    if (x % 2 == 0) return false;
    // 2y + 1
    if (x > 1) s = s + s + s;
  } else {
    if (x % 2 != 0) return false;
    if (x % 4 == 0) return false;
    // 4y + 2
    if (x == 2) {
      s += s;
    } else {
      s += s;
      s = s + s + s;
    }
  }
  int len = s.length();
  int i = 0;
  z = 1;
  while (i < len) {
    z = mul(z, convert(s[i]));
    if (z == 2) break;
    i++;
  }
  if (i >= len) return false;
  int l1 = i+1;
  i = len - 1;
  z = 1;
  while (i >= 0) {
    z = mul(convert(s[i]), z);
    if (z == 4) break;
    i--;
  }
  if (i < 0) return false;
  int l2 = len - i;
  return x * n > l1 + l2;
}

int main()
{
  int tcase = 0;
  ifstream fin("z.in");
  ofstream fout("z.out");
  fin >> tcase;
  for (int tind = 1; tind <= tcase; tind++) {
    int n;
    long long x;
    fin >> n >> x >> s;
    if (check(n, x)) {
      fout << "Case #" << tind << ": YES" << endl;
    } else {
      fout << "Case #" << tind << ": NO" << endl;
    }
  }
  return 0;
}
