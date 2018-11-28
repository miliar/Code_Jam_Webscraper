#include <cmath>
#include <cstdio>
#include <iostream>

using namespace std;

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  int T;
  cin >> T;
  for(int t = 1; t <= T; t++) {
    double C, F, X;
    cin >> C >> F >> X;

    int k = ceil(X/C);
    double time = X/2.0, buy = 0;
    for(int i = 1; i <= k; i++) {
      buy += C/(2.0+(i-1)*F);
      double total = buy+X/(2+i*F);
      time = min(time, total);
    }
    printf("Case #%d: %.7f\n", t, (float)time);
  }

  
  return 0;
}
