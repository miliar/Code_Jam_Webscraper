#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
double res[500][500];
int main() {
  ios_base::sync_with_stdio(0);
  int T, N, K;
  cin >> T;
  for (int t=1; t<=T; t++) {
    cout << "Case #" << t << ": ";
    cin >> N >> K;
    double p[N];
    for (int i=0; i<N; i++) cin >> p[i];
    sort(p, p+N);
    double ans = 0;
    for (int i=0; i<=K; i++) {
      int j = N-(K-i);
      vector<double> x;
      for (int k=0; k<i; k++) x.push_back(p[k]);
      for (int k=j; k<N; k++) x.push_back(p[k]);

      for (int k=0; k<2*K; k++) res[K-1][k] = 0;
      res[K-1][K-1] = 1 - x.back();
      res[K-1][K] = 0;
      res[K-1][K+1] = x.back();
      for (int k=K-2; k>=0; k--) {
        for (int l=1; l<2*K-1; l++) {
          res[k][l] = x[k] * res[k+1][l-1] + (1-x[k]) * res[k+1][l+1];
        }
      }
      ans = max(ans, res[0][K]);
    }
    cout.setf(ios::fixed);
    cout.precision(12);
    cout << ans << "\n";
  }
  return 0;
}
