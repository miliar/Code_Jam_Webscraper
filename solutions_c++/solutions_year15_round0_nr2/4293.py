#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool possible(vector<int> pancakes, int minutes) {
  for (int special_min = 0; special_min < minutes; special_min++) {
    int max_pancakes = minutes - special_min;
    int special_min_required = 0;
    for (int i = 0; i < pancakes.size(); i++)
      special_min_required += (pancakes[i] - 1) / max_pancakes;
    if (special_min_required <= special_min)
      return true;
  }
  return false;
}

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int D;
    cin >> D;

    // Upper bound on number of minutes needed to eat all pancakes.
    int max_minutes = 0;
    vector<int> pancakes;
    for (int i = 0; i < D; i++) {
      int pancake;
      cin >> pancake;
      max_minutes = max(max_minutes, pancake);
      pancakes.push_back(pancake);
    }

    int lower = 1, upper = max_minutes;
    while (lower < upper) {
      int mid = (lower + upper) / 2;
      possible(pancakes, mid) ? upper = mid : lower = mid + 1;
    }
    printf("Case #%d: %d\n", t, lower);
  }
  return 0;
}
