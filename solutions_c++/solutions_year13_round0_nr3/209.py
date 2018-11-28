#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>

#define LARGE_MODE true

#define MAX 10000001ULL
#define LEN 50000

using namespace std;

#ifdef LARGE_MODE
typedef string big;
#else
typedef unsigned long long int big;
#endif

int cnt = 0;
big fas[LEN];

#ifdef LARGE_MODE

bool cmp(big a, big b) {
  if (a.length() != b.length())
    return a.length() < b.length();

  for (int i = 0; i < a.length(); i++)
    if (a[i] < b[i])
      return true;
    else if (a[i] > b[i])
      return false;

  return false;
}

void gen_fas() {
  cin >> cnt;
  for (int i = 0; i < cnt; i++)
    cin >> fas[i];
}

#else

bool pal(big i) {
  big p = 0ULL, j = i;
  while (j != 0ULL) {
    p = (p * 10) + (j % 10);
    j /= 10;
  }

  return p == i;
}

bool cmp(big a, big b) {
  return a < b;
}

void gen_fas() {
  fas[cnt++] = 0;
  for (big i = 1; i < MAX; i++)
    if (pal(i) && pal(i * i))
      fas[cnt++] = i * i;
}

#endif

int bin_search(int lo, int hi, big t, bool eq) { // [lo, hi)
  if (lo + 1 >= hi)
    return lo;

  int mid = (lo + hi) / 2;
  if (!eq && cmp(t, fas[mid]))
    return bin_search(lo, mid, t, eq);
  else if (eq && !cmp(fas[mid], t))
    return bin_search(lo, mid, t, eq);
  else
    return bin_search(mid, hi, t, eq);
}

int main() {
  gen_fas();

  int ncases;
  big a, b;
  cin >> ncases;
  for (int caseno = 1; caseno <= ncases; caseno++) {
    cin >> a >> b;
    printf("Case #%i: %i\n", caseno, bin_search(0, cnt, b, false) - bin_search(0, cnt, a, true));
  }
}
