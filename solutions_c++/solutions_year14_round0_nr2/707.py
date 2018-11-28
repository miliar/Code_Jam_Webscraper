// mars.ma
#include <iostream>
#include <algorithm>
#include <iomanip>

using namespace std;

int main(void)
{
  int testcase;
  cin >> testcase;
  cout.setf(ios::fixed);
  for (int tc = 1; tc <= testcase; tc++) {
    double cost, farm, extra;
    cin >> cost >> farm >> extra;
    double result = extra/2;  // don't build any farm
    double build = 0;  // time used for build farms
    
    // find the limitation of the count of farms, balance point:
    // C/(2+F*N) + X/(F*(N+1)) = X/(2+F*N)
    int limit = (int)((farm*extra - 2*cost - cost*farm)/(cost*farm));
    limit += 100;  // protect for safe margin
    for (int count = 0; count < limit; ++count) {
      double speed = 2+farm*count;  // production speed
      result = min(result, build+(extra/speed));
      build += cost/speed;
    }

    cout << "Case #" << tc << ": " << setprecision(7) << result << endl;
  }

  return 0;
}

