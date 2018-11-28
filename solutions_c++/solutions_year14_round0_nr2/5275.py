#include <bits/stdc++.h>

#define each(i, c) for (auto& i : c)
#define unless(cond) if (!(cond))

using namespace std;

typedef long long int lli;
typedef unsigned long long ull;
typedef complex<double> point;

int main(int argc, char *argv[])
{
  int tc;
  cin >> tc;
  while (tc--) {
    double c, f, x;
    cin >> c >> f >> x;

    double p = 2;
    double time = 0;
    double mn = time + x / p;

    for (int loop = 0; loop < 100000000; ++loop) {
      time += (c / p);
      p += f;
      mn = min(mn, time + x / p);
    }

    static int cnt = 0;
    printf("Case #%d: %.7f\n", ++cnt, mn);
  }
  return 0;
}
