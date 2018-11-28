#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <string>
#include <climits>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <list>
#include <ctime>

#define PI 3.14159265358979
#define EPS 1e-9

using namespace std;

#define FOR(i, m, n) for (int i=m; i<n; i++)
#define ABS(a) (((a)>0)?(a):(-(a)))
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> ii;

int mat[200][200];
int N, M;
int row[200];
int coll[200];

void solve() {
	bool ans = true;
	scanf("%d%d", &N, &M);
	FOR (i, 0, N)
		FOR (j, 0, M) {
		scanf("%d", &mat[i][j]);
	}
	FOR (i, 0, N) {
		row[i] = 0;
		FOR (j, 0, M)
			row[i] = max(row[i], mat[i][j]);
	}
	FOR (j, 0, M) {
		coll[j] = 0;
		FOR (i, 0, N)
			coll[j] = max(coll[j], mat[i][j]);
	}
	FOR (i, 0, N) FOR (j, 0, M) {
		if (mat[i][j] < row[i] && mat[i][j] < coll[j]) {
			ans = false;
			goto vysl;
		}
	}
vysl:
	if (ans) printf("YES\n");
	else printf("NO\n");
}

int main()
{
  int t; scanf("%d", &t);
  FOR (i, 0, t) {
	  printf("Case #%d: ", i+1);
	  solve();
  }
  return 0;
}
