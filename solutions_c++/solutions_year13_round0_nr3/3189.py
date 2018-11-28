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
#define UI unsigned int
#define LLU unsigned long long


bool is_p(UI n) {
  stringstream ss;
  ss.clear();
  ss << n;
  string str = ss.str();
  size_t s = str.size();
  for (size_t i = 0; 2*i < s; ++i) {
    if (str[i] != str[s - i - 1]) {
      return false;
    }
  }
  return true;
}

int main() {
  // Declare members
  int num_case;
  cin >> num_case;

  int A, B;
  int count;

  for (int nc = 1; nc <= num_case; ++nc) {
    // Init members
    cin >> A;
    cin >> B;
    count = 0;

    int a = ceil(sqrt(A));
    int b = floor(sqrt(B));

    for (int i = a; i <= b; ++i) {
      if (is_p(i) && is_p(i*i)) {
        ++count;
      }
    }

    // Print output for case j
    cout << "Case #" << nc << ": " << count << endl;
  }


  return 0;
}
