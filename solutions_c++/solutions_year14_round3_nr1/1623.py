#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
using namespace std;

bool sanitize(long long &P, long long &Q)
{
  long long root = sqrt(Q);
  for (int i = 3; i <= root + 1; ++i) {
    if (i % 2 == 0) continue;
    if (Q % i == 0) {
      if (P % i != 0) {
        return false;
      }
      Q /= i;
      P /= i;
    }
  }
  return true;
}

int solve(long long P, long long Q)
{
  int level = 1;
  while (2 * P < Q) {
    Q /= 2;
    level++;
  }
  return level;
}

bool test(long long Q)
{
  while (Q > 1) {
    if (Q % 2 != 0) return false;
    Q /= 2;
  }
  return true;
}

int main()
{
  int T; cin >> T;
  for (int t = 1; t <= T; ++t) {
    long long P,Q;
    cin >> P >> Q;
    while (P % 2 == 0 && Q % 2 == 0) { P /= 2; Q /= 2; }
    if (P > Q || !sanitize(P,Q) || !test(Q))
      cout << "Case #" << t << ": impossible" << endl;
    else
      cout << "Case #" << t << ": " << solve(P,Q) << endl;
  }
  return 0;
}
