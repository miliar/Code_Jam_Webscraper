#include <cmath>
#include <iomanip>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

namespace {

double SolveSmall(vector<int> x, vector<int> y, vector<int> z) {
  const int N = x.size();
  vector<vector<double>> dist(N, vector<double>(N));
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < N; ++j) {
      dist[i][j] = sqrt((x[i] - x[j]) * (x[i] - x[j]) +
                        (y[i] - y[j]) * (y[i] - y[j]) +
                        (z[i] - z[j]) * (z[i] - z[j]));
    }
  }
  vector<double> d0(N, dist[0][1]);
  priority_queue<pair<double, int>> pq;
  pq.emplace(0.0, 0);
  while (!pq.empty()) {
    double d = -pq.top().first;
    int n = pq.top().second;
    pq.pop();
    if (d0[n] < d) continue;
    d0[n] = d;
    for (int i = 0; i < N; ++i) {
      double m = max(d, dist[n][i]);
      if (m < d0[i]) pq.emplace(-m, i);
    }
  }
  return d0[1];
}

double Solve(int S, vector<int> x, vector<int> y,vector<int> z, vector<int> vx, vector<int> vy, vector<int> vz) {
  return SolveSmall(x, y, z);
}

}

int main(void) {
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    int N, S;
    cin >> N >> S;
    vector<int> x(N), y(N), z(N), vx(N), vy(N), vz(N);
    for (int j = 0; j < N; ++j) {
      cin >> x[j] >> y[j] >> z[j] >> vx[j] >> vy[j] >> vz[j];
    }
    cout << "Case #" << i << ": " << setprecision(9) << Solve(S, x, y, z, vx, vy, vz) << endl;
  }

  return 0;
}
