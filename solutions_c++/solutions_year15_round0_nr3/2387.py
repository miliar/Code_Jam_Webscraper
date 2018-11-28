#include <cstdio>
#include <cassert>
#include <cstring>

#include <algorithm>
#include <iostream>

using namespace std;
typedef long long llint;

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define TRACE(x) cout << #x << " = " << x << endl
#define _ << " _ " <<


enum {Z, E, I, J, K};

int table[5][5] = {
  {Z, Z, Z, Z, Z},
  {Z, E, I, J, K},
  {Z, I, -E, K, -J},
  {Z, J, -K, -E, I},
  {Z, K, J, -I, -E}
};
int sgn(int x) { return x < 0 ? -1 : +1; }
int mul(int a, int b) {
  assert(a != Z);
  assert(b != Z);
  return sgn(a) * sgn(b) * table[abs(a)][abs(b)];
}

int power(int a, llint k) {
  int ret = E;
  for (int i = 0; (1LL << i) <= k; ++i) {
    if (((k >> i) & 1) == 1)
      ret = mul(ret, a);
    a = mul(a, a);
  }
  return ret;
}

int parse(char c) {
  int a;
  if (c == 'i') a = I;
  else if (c == 'j') a = J;
  else a = K;
  return a;
}

const int MAXL = 10005;
char s[11 * MAXL];

void solve() {
  int L; llint X;
  scanf("%d%lld", &L, &X);
  scanf("%s", s);

  int sp = E;
  REP(i, L) {
    int a = parse(s[i]);
    sp = mul(sp, a);
  }

  sp = power(sp, X);
  if (sp != mul(I, mul(J, K))) {
    puts("NO");
    return;
  }

  FOR(i, 1, 10) REP(j, L) 
    s[j + i * L] = s[j];

  if (X <= 9) {
    int l = -1;
    int p = E;
    for (int i = 0; i < X * L; ++i) {
      p = mul(p, parse(s[i]));
      if (p == I) { l = i; break; }
    }

    if (l == -1) {
      puts("NO");
      return;
    }

    int r = -1;
    p = E;
    for (int i = X * L - 1; i >= 0; --i) {
      p = mul(parse(s[i]), p);
      if (p == K) { r = i; break; }
    }

    if (r == -1 || l >= r) {
      puts("NO");
      return;
    }

    puts("YES");
    return;
  }

  bool ok = false;
  int p = E;
  for (int i = 0; i < 4 * L; ++i) {
    p = mul(p, parse(s[i]));
    if (p == I) ok = true;
  }

  if (!ok) {
    puts("NO");
    return;
  }

  ok = false;
  p = E;
  for (int i = 4 * L - 1; i >= 0; --i) {
    p = mul(parse(s[i]), p);
    if (p == K) ok = true;
  }

  if (!ok) {
    puts("NO");
    return;
  }

  puts("YES");
}

int main(void) 
{
  int T; scanf("%d", &T);
  for (int t = 1; t <= T; ++t) {
    printf("Case #%d: ", t);
    solve();
  }
  return 0;
}
