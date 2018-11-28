#include <cstdio>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <list>
using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

#define REP(x, n) for(int x = 0; x < (n); ++x)
#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define VAR(v, n) __typeof(n) v = (n)
#define FOREACH(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define SIZE(x) ((int)(x).size())
#define PB push_back
#define PF push_front
#define MP make_pair
#define FI first
#define SE second

const int INF = 1000000001;
const double EPS = 10e-9;

const int MAXN = 128;
int test_cases, n, m, t[MAXN][MAXN], row_max[MAXN], col_max[MAXN];
bool result;


int main() {

  scanf("%d", &test_cases);
  FOR(test_case, 1, test_cases) {

    REP(i,MAXN) row_max[i] = col_max[i] = 0;

    scanf("%d%d", &n, &m);
    REP(i,n) REP(j,m) {
    	scanf("%d", &t[i][j]);

      row_max[i] = max(row_max[i], t[i][j]);
      col_max[j] = max(col_max[j], t[i][j]);
    }


    result = true;
    REP(i,n) REP(j,m) if((t[i][j] < row_max[i]) && (t[i][j] < col_max[j])) result = false;


    printf("Case #%d: %s\n", test_case, (result)?"YES":"NO");
  }

  return 0;
}