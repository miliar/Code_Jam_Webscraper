#include <iostream>
#include <algorithm>

using namespace std;
typedef long long NumberType;
const NumberType MAX_N = 1414213567;

bool judge(NumberType r, NumberType t, NumberType n)
{
  return ((2*n*n + (2*r - 1)*n) <= t);
}

int main(void)
{
  int testcase;
  cin >> testcase;
  for (int tc = 1; tc <= testcase; tc++) {
    NumberType r, t;
    cin >> r >> t;
    NumberType max_n = min(2*t/r, MAX_N);
    NumberType min_n = 0;
    while (min_n < max_n) {
      NumberType middle = (max_n+min_n)/2;
      if (judge(r, t, middle)) {
        min_n = middle+1;
      } else {
        max_n = middle;
      }
    }

    NumberType result = 0;
    for (NumberType i = max_n+1; 0 <= i; i--) {
      if (judge(r, t, i)) {
        result = i;
        break;
      }
    }

    cout << "Case #" << tc << ": " << result << endl;
  }

  return 0;
}

