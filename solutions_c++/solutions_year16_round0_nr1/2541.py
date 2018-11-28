#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstring>
#include <string>
#include <map>
#include <queue>
#include <set>

#define LL long long int
#define FOR(i, s, e) for (int i=(s); i<(e); i++)
#define FOE(i, s, e) for (int i=(s); i<=(e); i++)
#define CLR(x, a) memset(x, a, sizeof(x))

using namespace std;

int test, n, b[10];

int main(){
	scanf("%d", &test);
	FOR(tc, 0, test) {
		scanf("%d", &n);
		printf("Case #%d: ", tc + 1);
		if (n == 0) printf("INSOMNIA\n");
		else {
			CLR(b, 0);
			int x = n;
			while (1) {
				int t = x;
				while (t) { b[t % 10] = 1; t /= 10; }
				int ok = 1;
				FOR(i, 0, 10) if (!b[i]) ok = 0;
				if (ok) break;
				x += n;
			}
			printf("%d\n", x);
		}
	}
	return 0;
}
