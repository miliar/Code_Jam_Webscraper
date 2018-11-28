#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cassert>

using namespace std;

int main(void)
{
  int testcase;
  cin >> testcase;
  for (int tc = 1; tc <= testcase; tc++) {
    int engery, regain, n;
    cin >> engery >> regain >> n;
    vector<int> values;
    for (int i = 0; i < n; i++) {
      int v;
      cin >> v;
      values.push_back(v);
    }

    int valueSz = values.size();
    assert(n == valueSz);
    int range = engery+1;
    int limit = (int)pow(range, valueSz);
    int result = 0;
    for (int i = 0; i < limit; i++) {
      int value = i;
      int gain = 0;
      int current = engery;
      bool valid = true;
      for (int j = 0; j < valueSz; j++) {
        int remain = value % range;
        value /= range;
        if (current < remain) {
          valid = false;
          break;
        }
        current -= remain;
        current += regain;
        current = min(current, engery);
        gain += values[j]*remain;
      }

      if (valid) {
        result = max(result, gain);
      }
    }

    cout << "Case #" << tc << ": " << result << endl;
  }

  return 0;
}

