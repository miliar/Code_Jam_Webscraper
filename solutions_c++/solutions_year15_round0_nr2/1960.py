#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solve_case(int case_id) {
  int n; cin >> n;
  vector<int> plates(n);
  for (int &x: plates) { cin >> x; }
  sort(plates.rbegin(), plates.rend());

  int best_time = plates[0];
  for (int h = 1; h <= plates[0]; ++h) {
    int time = 0;
    for (int x: plates) {
      time += (x/h);
      if (x % h == 0) { time -= 1; }
    }
    best_time = min(best_time, time + h);
  }

  cout << "Case #" << case_id << ": " << best_time << endl;
}

int main() {
  int t; cin >> t;
  for (int i = 1; i <= t; ++i) {
    solve_case(i);
  }
  return 0;
}
