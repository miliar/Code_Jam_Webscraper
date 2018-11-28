#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <algorithm>
using namespace std;

typedef unsigned long long ull;
typedef long long ll;

const int N = 1005;

double a[N], b[N];
int n;

int solve(double* a, double* b) {
  bool vis[N] = {0};
  int cnt = 0;
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      if (!vis[j] && a[i] < b[j]) {
        ++cnt;
        vis[j] = 1;
        break;
      }
    }
  }
  return cnt;
}

int main() {
  freopen("D-large.in", "r", stdin);
  freopen("out.txt", "w", stdout);

  int t, cases = 0;
  cin >> t;

  while (t--) {
    cin >> n;
    for (int i = 0; i < n; ++i)
      cin >> a[i];
    for (int j = 0; j < n; ++j)
      cin >> b[j];

    sort(a, a+n);
    sort(b, b+n);
    cout << "Case #" << ++cases << ": ";
    cout << solve(b, a) << " " << n-solve(a, b) << endl; 
  }
  return 0;
} 
