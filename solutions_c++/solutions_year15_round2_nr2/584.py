#include <iostream>
#include <vector>

using namespace std;

typedef long long int ll;

int buck[16];
int h, opt;
int n, m, k;

int abs(int x) {
  return x > 0 ? x : -x;
}

void check() {
  int r = 0;
  for (int i = 0; i < k; ++i) {
    for (int j = i + 1; j < k; ++j) {
      if (abs((buck[i] % n) - (buck[j] % n)) == 1 and (buck[i] / n) == (buck[j] / n)) ++r;
      if (abs((buck[i] / n) - (buck[j] / n)) == 1 and (buck[i] % n) == (buck[j] % n)) ++r;
    }
  }
  if (r < opt) opt = r;
}

void bt(int p, int u) {
  if (p == k) {
    check();
    return;
  }
  for (int i = u + 1; k - p <= h - i; ++i) {
    buck[p] = i;
    bt(p + 1, i);
  }
}

int main() {
  int tt;
  cin >> tt;
  for (int t = 1; t <= tt; ++t) {
    cout << "Case #" << t << ": ";
    cin >> n >> m >> k;
    h = n * m;
    opt = 1e9;
    bt(0, -1);
    cout << opt << endl;
  }
}