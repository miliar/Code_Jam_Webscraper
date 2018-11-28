#include <algorithm>
#include <iomanip>
#include <iostream>
#include <vector>

using namespace std;

vector<double> seconds_to_get_N_farms(double cookie_rate, double farm_rate, double farm_cost, int max_N) {
  vector<double> results;
  results.push_back(0);
  for (int i = 1; i <= max_N; i++) {
    double prod_rate = cookie_rate + (i - 1) * farm_rate;
    results.push_back(results[i - 1] + farm_cost/prod_rate);
  }

  return results;
}

int main(int argc, char *argv[]) {
  int T;
  cin >> T;

  for (int i = 1; i <= T; i++) {
    double C;
    cin >> C;

    double F;
    cin >> F;
    
    double X;
    cin >> X;

    vector<double> farm_times = seconds_to_get_N_farms(2.0, F, C, 100000);
    vector<double> total_times;
    for (int i = 0; i < farm_times.size(); i++) {
      total_times.push_back(farm_times[i] + X/(2.0 + F * i));
    }

    cout << fixed << setprecision(7) << "Case #" << i << ": " << *min_element(total_times.begin(), total_times.end()) << endl;
  }

  return 0;
}
				
