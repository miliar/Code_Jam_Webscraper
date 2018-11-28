
#include <iostream>
#include <vector>

#include <cassert>

using namespace std;

double combine(const std::pair<double, double> &high,
               const std::pair<double, double> &low, double X, double V) {
  double Vlow = -V * (X - high.second) / (high.second - low.second);
  double Vhigh = V - Vlow;

  double max_time = max(Vhigh / high.first, Vlow / low.first);

  // double high_diff = high.second - X;
  // double low_diff = X - low.second;

  // // printf("%f %f\n", high_diff, low_diff);

  // double ratio_high = high_diff / low_diff;
  // printf("%f\n", ratio_high);

  // double ratio_low = 1 / ratio_high;
  // double total = ratio_high + ratio_low;

  // double volume_high = V / total * ratio_high;
  // double volume_low = V / total / ratio_low;

  // double max_time = max(volume_high / high.first, volume_low / low.first);

  return max_time;
  // return 0;
}

int main() {
  int T;
  cin >> T;

  double epsilon = 1e-8;

  for (int test = 1; test <= T; test++) {
    int N;
    double V, X;
    cin >> N >> V >> X;

    std::vector<std::pair<double, double>> perfect, low, high;

    for (int i = 0; i < N; i++) {
      std::pair<double, double> source;

      cin >> source.first >> source.second;

      if (source.second > X + epsilon) {
        high.push_back(source);
      } else if (source.second < X - epsilon) {
        low.push_back(source);
      } else {
        perfect.push_back(source);
      }
    }

    assert(N <= 2);

    if (perfect.size() == 0 && high.size() != low.size()) {
      printf("Case #%d: %s\n", test, "IMPOSSIBLE");
      continue;
    }

    double fill_time = 0;
    if (perfect.size() > 0) {
      double total_rate = 0;
      for (auto &src : perfect) {
        total_rate += src.first;
      }
      fill_time = V / total_rate;
    } else {
      fill_time = combine(high[0], low[0], X, V);
    }
    printf("Case #%d: %f\n", test, fill_time);
  }
}