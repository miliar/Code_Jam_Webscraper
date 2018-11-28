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

int n, TC, r,c ;

void solve(int tc) {
	scanf("%d%d%d", &n, &r, &c);
	if (r > c) swap(r, c);
	int ok = 1;
	if (n > c) ok = 0;
	if (n > r * r && n > 2) ok = 0;
	if ((r * c) % n != 0) ok = 0;
	if (n == 4 && (r == 2 && c == 4)) ok = 0;
	printf("Case #%d: %s\n", tc, ok ? "Gabriel":"Richard");
}

int main(){
	scanf("%d", &TC);
	FOE(i, 1, TC) solve(i);
	return 0;
}

