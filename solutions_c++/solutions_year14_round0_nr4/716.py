// mars.ma
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int main(void)
{
  int testcase;
  cin >> testcase;
  for (int tc = 1; tc <= testcase; tc++) {
    int n;  cin >> n;
    vector<double> naomi(n);
    vector<double> ken(n);
    for (int i = 0; i < n; ++i) { cin >> naomi[i]; }
    for (int i = 0; i < n; ++i) { cin >> ken[i]; }

    set<double> kenset(ken.begin(), ken.end());
    int normal = 0;
    for (const auto& block : naomi) {
      auto it = kenset.upper_bound(block);
      if (kenset.end() == it) {
        it = kenset.upper_bound(0);
      }

      normal += (*it < block);
      kenset.erase(it);
    }

    sort(naomi.begin(), naomi.end());
    sort(ken.begin(), ken.end());

    int deceit = 0;
    int max1 = n-1, max2 = n-1, min1 = 0, min2 = 0;
    // greedy algorithm
    for (int i = 0; i < n; ++i) {
      if (ken[max2] < naomi[max1]) {
        deceit++;
        max1--;
        max2--;
      } else if (naomi[max1] < ken[max2]) {
        min1++;
        max2--;
      } else {
        if (ken[min2] < naomi[min1]) {
          deceit++;
          min1++;
          min2++;
        } else {
          min1++;
          max2--;
        }
      }
    }

    cout << "Case #" << tc << ": " << deceit << ' ' << normal << endl;
  }

  return 0;
}

