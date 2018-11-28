#include "stdio.h"
#include "stdlib.h"
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <climits>
#include <algorithm>
using namespace std;

typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int,int> PII;

#define REP(i,a) for(typeof(a) i = 0; i < (a); ++i)
#define FOR(i,a,b) for(typeof(a) i = (a); i < (b); ++i)
#define SZ(x) ((int)((x).size()))
#define ALL(c) (c).begin(), (c).end()
#define PB push_back
#define MP make_pair
#define GET_BITS(i,j) (i >> (j)) & 1
#define min(a,b) ((a) < (b) ? (a) : (b))
#define READI(n,a) REP(i,n) scanf("%d", &a[i]);

int main()
{
#ifdef DEBUG
  freopen("B-large.in", "r", stdin);
  freopen("a.out", "w", stdout);
#endif

  int T;
  cin >> T;
  REP(i,T)
  {
    double c,f,x;
    cin >> c >> f >> x;
    double kd =  (x*f - 2*c - 2*c*f) / (c * f);
    int k = (int)floor(kd + 1);

    double res = 0.0;
    if (k < 0)
    {
      res = x / 2.0;
    } else {
      REP(j,k+1) res += c / (2 + j * f);
      res += x / (2 + (k+1)*f);
    }
    printf("Case #%d: %0.7f\n", i + 1, res);
  }

  return 0;
}

