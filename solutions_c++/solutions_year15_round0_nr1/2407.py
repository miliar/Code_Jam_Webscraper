#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdlib>
#include <cstring>
#include <string>

#define FOR(i, s, e) for (int i=(s);i<(e);i++)
#define FOE(i, s, e) for (int i=(s);i<=(e);i++)
#define FOD(i, s, e) for (int i=(s)-1;i>=(e);i--)
#define CLR(x, a) memset(x, a, sizeof(x))
#define LL long long int
using namespace std;

int n, TC;
char s[10005];

void solve(int tc) {
	scanf("%d%s", &n, s);
	int cur = 0, ret = 0;
	FOR(i, 0, n + 1) {
	    if (cur < i) ret += (i - cur), cur = i;
	    cur += s[i] - '0';
	}
	printf("Case #%d: %d\n", tc, ret);
}

int main(){
	scanf("%d", &TC);
	FOE(i, 1, TC) solve(i);
	return 0;
}

