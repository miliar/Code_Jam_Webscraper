#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <ctime>
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>

#define sz(c) ((int)(c).size())
#define all(c) (c).begin(), (c).end()

using namespace std;
typedef double dbl;

void testCase()
{
  dbl c, f, x;
  cin >> c >> f >> x;

  dbl v = 2, t = 0;
  while (true)
  {
    dbl time1 = t + x / v;
    dbl time2 = t + c / v + x / (v + f);
    if (time1 <= time2)
    {
      printf("%.12f\n", time1);
      return;
    }
    t += c / v;
    v += f;
  }
}

int main() {
//  freopen("input.txt", "rt", stdin);
//  freopen("output.txt", "wt", stdout);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
//    cout << "Case #" << t << ": ";
    printf("Case #%d: ", t);
    testCase();
  }
  return 0;
}
