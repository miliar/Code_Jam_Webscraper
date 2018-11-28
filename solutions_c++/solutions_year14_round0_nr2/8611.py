#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <bitset>
#include <algorithm>
#include <utility>
#include <queue>
#include <iomanip>

using namespace std;
typedef long long ll;
typedef unsigned long long llu;
typedef vector<int> vi;
typedef vector<bool> vb;
typedef vector<ll> vl;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef map<int, int> mii;
typedef vector<double> vd;
typedef long double ld;

#define DFS_WHITE -1
#define DFS_BLACK 1
#define INF 1000000000

#define REP(i, n) for(int i=0; i < n; ++i)
#define SET(x, i) (x |= (1 << (i)))
#define UNSET(x, i) (x &= ~(1 << (i)))
#define GET(x, i) ((x) & (1 << (i)))

#define N 100

static const double epsilon = 0.00000001;

ld c,f,x;

ld tx(ld goal, ld cps)
{
  return goal/cps;
}

int main()
{
  int test_cases;
  scanf("%d", &test_cases);
  for(int t=1; t <= test_cases; ++t)
  {
    cin >> c >> f >> x;
    ld cps = 2;
    ld ct = 0;
    while(true)
    {
      if(tx(x, cps) < tx(x, cps+f)+tx(c, cps))
      {
        ct += tx(x, cps);
        break;
      }
      else
      {
        ct += tx(c, cps);
        cps += f;
      }
    }
    cout << "Case #" << t << ": " << std::setprecision(10) << std::fixed << ct << endl;
  }
}
