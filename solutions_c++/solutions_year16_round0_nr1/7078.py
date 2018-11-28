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


bool check_digits(set<int> &digits, LLU num) {
  while (num > 0) {
    digits.insert(num%10);
    num /= 10;
  }

  if (digits.size() >= 10) {
    return true;
  }
  return false;
}


int main() {
  // Declare members
  int num_case;
  cin >> num_case;


  for (int nc = 1; nc <= num_case; ++nc) {
    // Init members
    LLU orig;
    set<int> digits;

    cin >> orig;
    LLU last = orig;
    if (last == 0) {
      cout << "Case #" << nc << ": " << "INSOMNIA" << endl;
      continue;
    }

    while (!check_digits(digits, last)) {
      last += orig;
    }

    // Print output for case j
    cout << "Case #" << nc << ": " << last << endl;
  }


  return 0;
}
