#include <bits/stdc++.h>

using namespace std;

const int M = 5;

int n, a[M], b[M];
int table;
bool g[M][1 << M];


void read() {
  cin >> n;
  table = 0;
  for (int i = 0; i < n; ++i)
    for (int j = 0; j < n; ++j) {
      char c;
      cin >> c;
      if (c == '1')
        table |= 1 << (i * n + j);
    }
}


void read(int table) {
  fill(a, a + n, 0);
  fill(b, b + n, 0);
  for (int i = 0; i < n; ++i)
    for (int j = 0; j < n; ++j)
      if ((table >> (i * n + j)) & 1) {
        a[i] |= (1 << j);
        b[j] |= (1 << i);
      }
}


bool nice() {
  for (int ex = 0; ex < n; ++ex) {
    for (int mask = 0; mask < (1 << n); ++mask) {
      int t = 0;
      for (int k = 0; k < n; ++k)
        if ((mask >> k) & 1) {
          for (int i = 0; i < n; ++i)
            if (i != ex) 
              if ((a[i] >> k) & 1)
                t |= 1 << i;
        }
      g[ex][mask] = __builtin_popcount(mask) <= __builtin_popcount(t);
    }
  }

  for (int ex = 0; ex < n; ++ex) {
    for (int mask = 0; mask < (1 << n); ++mask)
      for (int i = 0; i < n; ++i)
        g[ex][mask | (1 << i)] &= g[ex][mask];
  }

  for (int i = 0; i < n; ++i)
    if (g[i][a[i]])
      return false;

  return true;
}


void kill() {
  int ans = n * n + 10;
  for (int mask = 0; mask < (1 << (n * n)); ++mask)
    if ((mask & table) == table) {
      read(mask);
      if (nice())
        ans = min<int>(ans, __builtin_popcount(mask));
    }
  
  ans -= __builtin_popcount(table);
  cout << ans << endl;
}


int main() {
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
