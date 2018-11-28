#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <string>
#include <string.h>
#include <queue>
#include <stack>
#include <deque>
#include <map>
#include <set>
#include <cmath>
#include <sstream>
#include <ctime>

#define pb push_back
#define mp make_pair
#define PI 3.1415926535897932384626433832795
#define ALL(x) x.begin(), x.end()
#define F first
#define S second
#define m0(x) memset(x,0,sizeof(x))
#define m1(x) memset(x,-1,sizeof(x))
#define pw(x) (1ull<<(x))

using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int,int> pii;
const int INF = 2147483647;
const ll LLINF = 9223372036854775807LL;

double calc(double c, double f, double x, int need) {
  double spent = 0;
  for (int i=0;i<need;i++) spent+=c/(2+i*f);
  return spent + x/(2+need*f);
}

int main() {
  //freopen("input.txt", "r", stdin);
  //freopen("output.txt", "w", stdout);
  cout << fixed << setprecision(8);
  int t;
  cin >> t;
  for (int te=0;te<t;te++) {
    double c,f,x;
    cin >> c >> f >> x;
    int l=0, r = 1000000;
    while (r-l>2) {
      int m1 = l+(r-l)/3;
      int m2 = l+2*(r-l)/3;
      double r1 = calc(c, f, x, m1), r2 =calc(c, f, x, m2);
      if (r1<r2) r = m2;
      else l = m1;
    }
    double ans = INF;
    for (int i=l;i<=r;i++) ans = min(ans, calc(c,f,x,i));

    cout << "Case #" << te+1 << ": " << ans << "\n";
  }
  return 0;
}
