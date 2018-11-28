#include <iostream>
#include <iomanip>
using namespace std;

double farm;
double farm_rate;
double cookies;

double Cookies() {
  double rate = 2.0;
  double min_time = cookies / rate;
  double cur_time = 0;

  while (cur_time < min_time) {
    min_time = min(min_time, cur_time + (cookies / rate));

    cur_time += (farm / rate);
    rate += farm_rate;
  }

  return min_time;
}

int main() {
  int ncases;
  cin >> ncases;
  for (int c = 1; c <= ncases; ++c) {
    cin >> farm >> farm_rate >> cookies;
    cout << "Case #" << c << ": " << fixed << setprecision(7) << Cookies() << "\n";
  }

  return 0;
}
