#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iomanip>
#include <algorithm>

using namespace std;

int main()
{
  ifstream in("/home/eric30/Eric/googlecodejam/2014/qualification/B-large.in");
  ofstream out("/home/eric30/Eric/googlecodejam/2014/qualification/b-large.out");

  if (in.is_open()) {
    int cases;
    in >> cases;

    for (int c = 1; c <= cases; ++c) {
      double time_used = 0.0;

      double farm_cost, farm_rate, target;
      in >> farm_cost >> farm_rate >> target;

      double rate = 2.0;

      while (true) {
        // Calculate time needed for two circumstacnes
        //  1. Stay tuned. Don't buy a farm.
        //  2. We need to buy a farm once we get enough cookies
        double time_dontbuy = target / rate;
        double time_buy = (farm_cost / rate) + (target / (rate + farm_rate));

        if (time_dontbuy < time_buy) {
          time_used += time_dontbuy;
          break;
        } else {
          time_used += farm_cost / rate;
          rate += farm_rate;
        }
      }

      out << "Case #" << c << ": " << fixed << setprecision(7) << time_used << endl;
    }
  }

  return 0;
}
