#include <bits/stdc++.h>

using namespace std;

typedef long double ld;

const int M = 207;

int n, k;
ld p[M];
ld d[M][M];
int m;

void ini() {
  m = 0;
  d[0][0] = 1.0;
}

void add(ld x) {
  ++m;
  for (int i = 0; i <= m; ++i) {
    int a = i, b = m - i;
    d[a][b] = 0.0;
    if (a > 0)
      d[a][b] += x * d[a - 1][b];
    if (b > 0)
      d[a][b] += (1 - x) * d[a][b - 1];
  }
}

ld fun(int a) {
  ini();
  for (int i = 0; i < a; ++i)
    add(p[i]);
  for (int i = 0; i < (k - a); ++i)
    add(p[n - 1 - i]);
  return d[k / 2][k / 2];
}


void read() {
  cin >> n >> k;
  for (int i = 0; i < n; ++i)
    cin >> p[i];
}

void kill() {
  sort(p, p + n);
  
  ld ans = fun(k / 2);
  //cerr << "bef : " << ans << endl;
  for (int i = 0; i <= k; ++i)
    ans = max(ans, fun(i));
  //cerr << "aft : " << ans << endl;
  cout << ans << endl;
}


int main() {
  cout.precision(9);
  cout << fixed;
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cout << "Case #" << i << ": ";
    read();
    kill();
    cerr << "Case #" << i << " done.\n";
  }
  return 0;
}
