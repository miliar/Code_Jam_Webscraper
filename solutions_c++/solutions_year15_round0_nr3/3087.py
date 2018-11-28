#include <iostream>
#include <cstring>
#include <vector>
#include <cmath>
using namespace std;

int mul(int a, int b) {
  if (a == 1) {
    if (b == 1) return 1;
    if (b == 2) return 2;
    if (b == 3) return 3;
    return 4;
  }
  if (a == 2) {
    if (b == 1) return 2;
    if (b == 2) return -1;
    if (b == 3) return 4;
    return -3;
  }
  if (a == 3) {
    if (b == 1) return 3;
    if (b == 2) return -4;
    if (b == 3) return -1;
    return 2;
  }
  if (a == 4) {
    if (b == 1) return 4;
    if (b == 2) return 3;
    if (b == 3) return -2;
    return -1;
  }
}

int op(int a, int b) {
  int x = mul(abs(a), abs(b));
  if (a < 0) x = -x;
  if (b < 0) x = -x;
  return x;
}

int convert(char c) {
  if (c == 'i') return 2;
  if (c == 'j') return 3;
  if (c == 'k') return 4;
}

int M[10005][10][10];

int rec(int p, int w, int x, vector<int>& v) {
  int& res = M[p][w][x + 5];
  if (res == -1) {
    if (w > 2) return res = 0;

    if (p == v.size()) {
      if (w == 2 and x == 4) return res = 1;
      return res = 0;
    }

    x = op(x, v[p]);
    res = 0;
    if (x == w + 2) res = rec(p + 1, w + 1, 1, v);
    res = max(res, rec(p + 1, w, x, v));
  }
  return res;
}

string solve() {
  int n, m;
  cin >> n >> m;
  vector<int> X(n);
  for (int i = 0; i < n; ++i) {
    char c;
    cin >> c;
    X[i] = convert(c);
  }
  vector<int> v;
  for (int i = 0; i < m; ++i) {
    for (int j = 0; j < n; ++j) v.push_back(X[j]);
  }

  memset(M, -1, sizeof(M));
  int ok = rec(0, 0, 1, v);
  if (ok) return "YES";
  return "NO";
}

int main() {
  int casos;
  cin >> casos;
  for (int cas = 1; cas <= casos; ++cas) {
    cout << "Case #" << cas << ": " << solve() << endl;
  }
}
