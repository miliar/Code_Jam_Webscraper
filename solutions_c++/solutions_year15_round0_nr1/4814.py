#include <iostream>
#include <iomanip>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <map>
#include <vector>
#include <set>


using namespace std;

#define PI acos(-1.)
#define EPS 1e-7
#define LL long long
#define U unsigned int
#define LU long unsigned
#define LLU long long unsigned




int main() {
  // Declare members
  int num_case;
  cin >> num_case;

  char c;
  int smax;
  int curr;
  int sum;
  int res;

  for (int nc = 1; nc <= num_case; ++nc) {
    // Init members
    sum = 0;
    res = 0;

    cin >> smax;
    for (int i = 0; i <= smax; ++i) {
      cin >> c;
      curr = atoi(&c);
      if (sum < i) {
        res += i - sum;
        sum += i - sum;
      }
      sum += curr;
    }

    // Print output for case j
    cout << "Case #" << nc << ": " << res << endl;
  }


  return 0;
}
