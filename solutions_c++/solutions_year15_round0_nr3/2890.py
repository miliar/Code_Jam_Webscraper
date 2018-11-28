#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int tab[256][256];

int mul(int a, int b) {
  int sign = 1;
  if (a < 0) { sign *= -1; a *= -1; }
  if (b < 0) { sign *= -1; b *= -1; }
  return tab[a][b] * sign;
}

int mpow(int val, int mexp) {
  if (mexp == 0) return '1';
  if (mexp == 1) return val;
  int half = mpow(val, mexp / 2);
  int squared = mul(half, half);
  return mexp % 2 ? mul(squared, val) : squared;
}

int main() {
  tab['1']['1'] = '1';
  tab['1']['i'] = 'i';
  tab['1']['j'] = 'j';
  tab['1']['k'] = 'k';
  tab['i']['1'] = 'i';
  tab['i']['i'] = -'1';
  tab['i']['j'] = 'k';
  tab['i']['k'] = -'j';
  tab['j']['1'] = 'j';
  tab['j']['i'] = -'k';
  tab['j']['j'] = -'1';
  tab['j']['k'] = 'i';
  tab['k']['1'] = 'k';
  tab['k']['i'] = 'j';
  tab['k']['j'] = -'i';
  tab['k']['k'] = -'1';

  int T;
  scanf("%d", &T);
  for (int tc = 1; tc <= T; tc++) {
    int L, X;
    char A[11111];
    scanf("%d %d %s", &L, &X, A);

    bool goodsum = false, found1 = false, found2 = false;

    int Lsum = '1';
    for (int i = 0; i < L; i++) Lsum = mul(Lsum, A[i]);
    int LXsum = mpow(Lsum, X);
    goodsum = (LXsum == -'1');

    string s;
    for (int i = 0; i < X && i < 10; i++) s.append(A);

    int val = '1';
    for (int i = 0; i < (int)s.size(); i++) {
      val = mul(val, s[i]);
      if (val == 'i') found1 = true;
      if (found1 && val == 'k') found2 = true;
    }

    printf("Case #%d: %s\n", tc, goodsum && found1 && found2 ? "YES" : "NO");
  }
}
