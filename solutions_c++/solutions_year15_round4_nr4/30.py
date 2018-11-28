/**
 * Author: Sergey Kopeliovich (Burunduk30@gmail.com)
 */

#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

typedef pair <int, int> pii;
typedef long long ll;

const int N = 1e6;
int r, c, res, a[6][6];
unordered_set<ll> was(N);

bool check( int y ) {
  forn(x, c) 
    if (a[y][x] != 
       (a[y][x] == a[y][(x + 1) % c]) +
       (a[y][x] == a[y][(x + c - 1) % c]) +
       (y + 1 < r  && a[y][x] == a[y + 1][x]) +
       (y - 1 >= 0 && a[y][x] == a[y - 1][x]))
     return 0;
  return 1;
}

ll getHash( ll dx ) {
  ll res = 0;
  forn(y, r)
    forn(x, c)
      res = res * 3 + a[y][(x + dx) % c];
  return res;
}

void go( int i, int j ) {
  //printf("%d, %d : %d, %d\n", r, c, i, j);
  if (j == c) {
    i++, j = 0;
    if (i >= 2 && !check(i - 2))
      return;
    if (i == r) {
      if (check(i - 1) && !was.count(getHash(0))) {
        res++;
        forn(i, c)
          was.insert(getHash(i));
      }
      return;
    }
  }
  for (int x = 1; x <= 3; x++) {
    a[i][j] = x;
    go(i, j + 1);
  }
}

int f() {
  res = 0;
  was.clear();
  go(0, 0);
  return res;
}

void solve() {
  static map<pii, int> m;
  cin >> r >> c;
  if (!m.count(pii(r, c)))
    m[pii(r, c)] = f();
  printf("%d\n", m[pii(r, c)]);
}

int main() {
  int tn;
  scanf("%d", &tn);
  was.rehash(N);
  forn(t, tn) {
    printf("Case #%d: ", t + 1);
    solve();
  }
  return 0;
}

