#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

int N, K;
vector<double> c;
double memo[201][201];

double doit(int i, int votes) {
  if (i == c.size()) {
    return (votes*2 == K) ? 1.0 : 0.0;
  }
  double& ret = memo[i][votes];
  if (ret != -1.0) return ret;
  ret = c[i]*doit(i+1, votes+1) + (1-c[i])*doit(i+1, votes);
//cout << i << ' ' << c[i] << ' ' << votes << ' ' << ret << endl;
  return ret;
}

int main() {
  int T, prob=1;
  for (cin >> T; T--;) {
    cin >> N >> K;
    cout << "Case #" << prob++ << ": ";
    vector<double> v(N);
    for (int i = 0; i < N; i++) cin >> v[i];
    sort(v.begin(), v.end());

    double ret = 0.0;
    for (int i = 0; i <= K; i++) {
      c.clear();
      for (int j = 0; j < i; j++) c.push_back(v[j]);
      for (int j = 0; j < K-i; j++) c.push_back(v[v.size()-1-j]);
      for (int j = 0; j <= K; j++)
      for (int k = 0; k <= K; k++)
        memo[j][k] = -1.0;
      ret = max(ret, doit(0, 0));
    }

    printf("%.9lf\n", ret);
  }
}
