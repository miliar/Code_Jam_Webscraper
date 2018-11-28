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
int tc, tcn,n;
bool ch[11];

void input() {

}

void solve() {
	scanf("%d", &tc);
	while (tc--) {
		scanf("%d", &n);
		for (int i = 0; i < 11; i++)
			ch[i] = 0;
		int re = 0, cnt = 0;
		if (n) {
			for (int i = 1; i <= 100; i++) {
				int t = i*n;
				while (t) {
					if (!ch[t%10]) {
						ch[t%10] = 1;
						cnt++;
					}
					t /= 10;
				}
				if (cnt == 10) {
					re = i*n;
					break;
				}
			}
		}
		printf("Case #%d: ",++tcn);
		if (!re)puts("INSOMNIA");
		else
			printf("%d\n", re);

	}
}

int main(void) {
	//freopen("AL.in", "r", stdin);
	//freopen("ALout.txt", "w", stdout);
	solve();
	return 0;
}