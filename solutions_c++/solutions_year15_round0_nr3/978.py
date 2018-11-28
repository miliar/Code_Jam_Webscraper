#include <cstdlib>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cassert>
#include <limits>
using namespace std;

#define FOR(i,n) for (int i = 0; i < n; ++i)
#define REP(i,n) for (int i = 1; i <= n; ++i)
#define FOREACHQ(q) for (int q = -K; q <= K; ++q) if (q != 0)

// quaternion definitions
enum {I = 2, J, K};
const int tab[5][5] = {
  {0, 0, 0, 0, 0},
  {0, 1, I, J, K},
  {0, I, -1, K, -J},
  {0, J, -K, -1, I},
  {0, K, J, -I, -1}
};
int tab2[9][9];

// quaternion operations
int mul(int l, int r)
{ // never put zero(s)
  int l0 = abs(l), r0 = abs(r);
  return (l / l0) * (r / r0) * tab[l0][r0];
}
int pow(int x, long p)
{
  assert(p >= 0);
  if (!(p % 4)) return 1;
  return mul(pow(x, p - 1), x);
}
int invr(int x, int y)
{// find z where x = zy
  return tab2[x + K][y + K];
}

/*
  will search one of the forms
  (I) * (J) * (K) = (U^a * b) * (c * U^d * e) * (f * U^g)
  which satisfies conditions
 */
int L; // <= 10^4
long X; // <= 10^12
int unit[10001]; // input string (length L)
int U; // the result of multiplication of unit[]
int U_postfix[10001]; // the result of multiplication of the last i quaternions of unit[]
int UcanXY[9][9], UcanXJY[9][9];

void init()
{
  FOREACHQ(a) FOREACHQ(b) tab2[mul(a, b) + K][b + K] = a;

  scanf(" %d %ld ", &L, &X);
  REP(i,L) {
    char c; scanf(" %c",&c);
    if (c == 'i')  unit[i] = I;
    else if (c == 'j') unit[i] = J;
    else if (c == 'k') unit[i] = K;
    else assert(false);
  }
  
  U_postfix[0] = 1;
  REP(i,L) U_postfix[i] = mul(unit[L - i + 1], U_postfix[i - 1]);
  U = U_postfix[L];

  FOREACHQ(a) FOREACHQ(b) UcanXY[a + K][b + K] = 0;
  for (int i = 0; i <= L; ++i) {
    int UU = U_postfix[L - i];
    UcanXY[invr(U, UU) + K][UU + K] = 1;
  }

  FOREACHQ(a) FOREACHQ(b) UcanXJY[a + K][b + K] = 0;
  for (int i = 0; i < L; ++i) {
    int XX = invr(U, U_postfix[L - i]);
    int YY;
    FOREACHQ(q) if (mul(XX, mul(J, q)) == U) { YY = q; break; }
    for (int j = 1; i + j <= L; ++j) {
      int k = L - i - j;
      if (U_postfix[k] == YY)
        UcanXJY[XX + K][YY + K] = 1;
    }
  }
}

bool test(int a, int b, int c, int d, int e, int f, int g)
{
 
  if (mul(pow(U,a), b) == I
      && mul(mul(c, pow(U, d)), e) == J
      && mul(f, pow(U, g)) == K) {

//     if (a == 1 && b == 3 && c == 2 && d == 1 && e == 1 && f == 1 && g == 3) {
//       puts("here");
//       printf("%d\n", UcanXY[b + K][c + K]);
//     }

    if (((b == 1 && c == 1) || UcanXY[b + K][c + K])
        && ((e == 1 && f == 1) || UcanXY[e + K][f + K])
        && X >= a + d + g + 2
        && !((X - (a + d + g + 2)) % 4))
      return true;

    if (UcanXJY[b + K][f + K]
        && X >= a + g + 1
        && !((X - (a + g + 1)) % 4))
      return true;
  }

  return false;
}

const char *solve()
{
  init();

  if (pow(U, X) != mul(mul(I, J), K))
    return "NO";

  FOR (a, 4) FOR (d, 4) FOR (g, 4) {
    FOREACHQ(b) FOREACHQ(c) FOREACHQ(e) FOREACHQ(f) {
      if (test(a, b, c, d, e, f, g)) return "YES";
    }
  }

  return "NO";
}

int main()
{
  int ncases;
  scanf(" %d", &ncases);
  REP(i, ncases)
    printf("Case #%d: %s\n", i, solve());

  return 0;
}
