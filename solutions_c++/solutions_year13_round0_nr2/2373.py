#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <cstdlib>
#include <map>
#include <queue>

#define LL long long int
#define FOR(i, s, e) for (int i=(s);i<(e);i++)
#define FOE(i, s, e) for (int i=(s);i<=(e);i++)
#define FOD(i, s, e) for (int i=(e)-1;i>=(s);i--)
#define CLR(x, a) memset(x, a, sizeof(x))

#define N 105
using namespace std;

int testcase;
int n, m, a[N][N], large, ok;

int main(){
	scanf("%d", &testcase);
	FOR(TC, 0, testcase){
		
		ok = 1;
		scanf("%d%d", &n, &m);
		FOR(i, 0, n) FOR(j, 0, m) scanf("%d", &a[i][j]);
		
		FOR(i, 0, n)
		FOR(j, 0, m){
			large = 0;
			FOR(k, 0, n)
				if (a[k][j] > a[i][j]) large = 1;
			if (!large) continue;
			large = 0;
			FOR(k, 0, m)
				if (a[i][k] > a[i][j]) large = 1;
			if (large) ok = 0;
		}
		
		printf("Case #%d: %s\n", TC + 1, (ok == 1)?"YES":"NO");
	}
	return 0;
}
