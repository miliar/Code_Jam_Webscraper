#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <set>
#include <deque>
#include <cmath>
#include <cstdlib>
#include <map>
#include <climits>
#include <limits>
#include <functional>
#include <bitset>
using namespace std;
#define LL long long
#define LD long double
#define mod 1000000007
int tc,tcn,n,d[101][2];
char s[101];

void input() {

}

void solve() {
	scanf("%d", &tc);
	while (tc--) {
		scanf("%s", s);
		n = strlen(s);
		for (int i = 0; i < n; i++) {
			if (!i) {
				if (s[i] == '-')
					d[i][0] = 0, d[i][1] = 1;
				else
					d[i][0] = 1, d[i][1] = 0;
			}
			else {
				if (s[i] == '-') {
					d[i][0] = min(d[i - 1][0], d[i - 1][1] + 1);
					d[i][1] = min(d[i - 1][0] + 1, d[i - 1][1] + 2);
				}
				else {
					d[i][0] = min(d[i - 1][0] + 2, d[i - 1][1] + 1);
					d[i][1] = min(d[i - 1][1], d[i - 1][0] + 1);
				}
			}
		}

		printf("Case #%d: %d\n", ++tcn, d[n - 1][1]);
	}
}

int main(void) {
	//freopen("BL.in", "r", stdin);
	//freopen("BLout.txt", "w", stdout);
	solve();
	return 0;
}