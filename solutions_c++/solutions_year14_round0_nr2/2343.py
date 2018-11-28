#include <iostream>
#include <set>
#include <tuple>
#include <iomanip>

using namespace std;

int t_;
double c, f, x, res;
double seconds, coins;
int farms;

int main() {
  freopen("input", "r", stdin);
  freopen("output", "w", stdout);
  cin >> t_;
  for (auto cas = 1; cas <= t_; cas++) {
    cin >> c >> f >> x;
    multiset < tuple <double, double, int> > Q;
    Q.insert(make_tuple(0, 0, 0));
    while (!Q.empty()) {
      tie(seconds, coins, farms) = *Q.begin();
      Q.erase(Q.begin());
      if (coins >= x) break;
      // Try to wait for enough coins to finish
      Q.insert(make_tuple(seconds + (x - coins) / (farms * f + 2), x, farms));
      if (coins >= c) {
        // Try to buy a farm
        Q.insert(make_tuple(seconds, coins - c, farms + 1));
      } else {
        // Try to wait for enough coins for another farm
        Q.insert(make_tuple(seconds + (c - coins) / (farms * f + 2), c, farms));
      }
    }
    cout << "Case #" << cas << ": ";
    cout.precision(6);
    cout << fixed << seconds << endl;
  }
  return 0;
}