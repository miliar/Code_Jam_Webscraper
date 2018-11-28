/** 
 *
 * rais.fathin38
 */

#include <cstdio>
#include <cstring>
#include <cmath>
#include <cassert>
#include <cstdlib>
#include <cctype>
#include <ctime>

#include <iostream>
#include <iomanip>
#include <sstream>
#include <numeric>
#include <utility>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <list>
#include <bitset>
#include <complex>

using namespace std;

#define ALL(a) a.begin(), a.end()
#define SZ(a) ((int)a.size())

#define MIN(a, b) a = min(a, b)
#define MAX(a, b) a = max(a, b)

#define SHOW(x) { cerr << ">>> " << #x << " : " << x << endl; }

#define pb push_back
#define mp make_pair
#define fi first
#define se second

typedef long long LL;
typedef pair<int, int> pii;

int main() {
  int T; scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    double c, f, x;
    scanf("%lf%lf%lf", &c, &f, &x);
    double ans = x/2.;
    double buy = 0;
    for (int i = 1; i <= 100000; i++) {
      buy += c/(2.+f*(i-1));
      MIN(ans, buy + x/(2.+f*i));
    }
    printf("Case #%d: %.7lf\n", t, ans);
  }
  return 0;
}

