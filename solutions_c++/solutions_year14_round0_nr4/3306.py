#include <iostream>
#include <algorithm>
using namespace std;

double x[1010], y[1010];

int opt1(int n) {
  int xi = n-1, yi = n-1, res = 0;
  for (int i = 0; i < n; i++) {
    if (x[xi] > y[yi]) res++;
    else yi--;
    xi--;
  }
  return res;
}

int opt2(int n, int k) {
  int xi = k, yi = 0, res = 0;
  for (int i = 0; i < n-k; i++) {
    if (x[xi] > y[yi]) { res++; yi++; }
    xi++;
  }
  return res;
}

int main() {
  int t; cin >> t;
  for (int c = 1; c <= t; c++) {
    int n; cin >> n;
    for (int i = 0; i < n; i++) cin >> x[i];
    for (int i = 0; i < n; i++) cin >> y[i];
    sort(x, x+n);
    sort(y, y+n);

    int a = opt1(n), b = 0;
    for (int i = 0; i < n; i++)
      b = max(b, opt2(n, i));
    cout << "Case #" << c << ": " << b << " " << a << endl;
  }
  return 0;
}
