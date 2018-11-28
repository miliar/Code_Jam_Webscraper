#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int encode(int n, const string &s) {
  int ret = 0;
  for (int i = 0; i < n; ++i)
    if (s[i] == 'X') ret |= (1 << i);
  return ret;
  }

double expLoss(int n, int mask, vector<double> &mem) {
  if (mask+1 != (1 << n)) {
    int hibit = (1 << (n-1));
    while (mask && !(mask & 1)) mask >>= 1;
    while (mask & hibit) mask = ((mask ^ hibit) << 1) ^ 1;
    }

  if (mem[mask] == -1) {
    mem[mask] = 0;
    for (int i = 0, k = 0; i < n; ++i)
      if (!(mask & (1 << i))) {
        double p = (k+1); p /= n;
        mem[mask] += p * (0.5*k + expLoss(n, mask | (1 << i), mem));
        k = 0;
        }
      else ++k;
    }
  return mem[mask];
  }

int main() {
  cout << fixed << setprecision(10);
  int nc; cin >> nc;
  for (int curC = 1; curC <= nc; ++curC) {
    string wheel; cin >> wheel;

    int n = wheel.size(), rem = count(wheel.begin(), wheel.end(), '.');
    vector<double> mem(1 << n, -1);
    mem.back() = 0;

    double ans = n*rem - expLoss(n, encode(n, wheel), mem);

    cout << "Case #" << curC << ": " << ans << '\n';
    }
  }

