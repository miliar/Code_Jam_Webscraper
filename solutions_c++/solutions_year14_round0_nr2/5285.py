#include <iostream>
#include <cstdio>

using namespace std;

int main(int argc, char* argv[]) {
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    //    cout << "Case #" << i << ": ";
    double C, F, X;
    cin >> C >> F >> X;
    int n = 0;
    double ans = X / 2;
    double nans = ans + (C - X) / (2 + n * F) + X / (2 + (n + 1) * F);
    while (nans < ans) {
      ans = nans;
      ++n;
      nans = ans + (C - X) / (2 + n * F) + X / (2 + (n + 1) * F);
    }
    printf("Case #%d: %.7f\n", i, ans);
  }
}
