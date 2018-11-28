#include "iostream"
#include "vector"
#include "algorithm"

int main() {
  int T;
  std::cin >> T;
  for (int t = 1; t <= T; ++t) {
    // std::cout << "Case #" << t << ": ";
    double C, F, X;
    std::cin >> C >> F >> X;
    // if buy farm, buy early
    // enumerate how many farm to buy in first several rounds
    // first, try never buy a farm
    double ans = X / 2;
    double speed = 2, time = 0;
    while (X/speed > C/speed + X/(speed+F)) {
      ans = std::min(ans, time + C/speed + X/(speed+F));
      time += C/speed;
      speed += F;
    }
    // std::cout << ans << std::endl;
    printf("Case #%d: %.7f\n", t, ans);
  }
  return 0;
}
