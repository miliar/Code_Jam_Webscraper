#include <iostream>
#include <algorithm>
#include <iomanip>
using namespace std;
void solve() {
  double C, F, X;
  cin >> C >> F >> X;

  double coin = C, speed = 2, escaped = min(C, X)/2;
  while(coin < X) {
    double escaped_if_no_farm = (X - coin) / speed;
    double escaped_if_buy_farm = X / (speed + F);
    if (escaped_if_buy_farm < escaped_if_no_farm) {
      coin = C;
      speed += F;
      escaped += C / speed;
    } else {
      coin = X;
      escaped += escaped_if_no_farm;
    }
  }
  cout << fixed << setprecision(9) << escaped << endl;
}
int main(int argc, char const *argv[])
{
  int coin, speed;
  int casn;
  cin >> casn;
  for (int i = 0; i < casn; ++i)
  {
    cout << "Case #" << i + 1 << ": ";
    solve();
  }
  return 0;
}
