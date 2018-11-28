#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <iostream>
#include <vector>
#include <ctime>
using namespace std;

int p, tot, s[1 << 21];
map <int, int> Map;
int T;

struct aa {
	int e, f;
} a[11000];

void solve() {
	int tot = 0;
	scanf("%d", &p);
	for (int i = 1; i <= p; i++)
		scanf("%d", &a[i].e);
	for (int i = 1; i <= p; i++)
		scanf("%d", &a[i].f), tot += a[i].f;
	Map.clear();
	for (int i = 1; i <= p; i++)
		Map[a[i].e] += a[i].f;
	Map[0]--;
	int n = 0;
	s[1] = 0;
	while ((1 << n) < tot) {
		int ans = 1e9;
		for (int i = 1; i <= p; i++)
			if (Map[a[i].e] > 0) ans = min(ans, a[i].e);
		printf(" %d", ans);
		for (int i = 1; i <= (1 << n); i++)
			Map[s[i] + ans]--, s[i + (1 << n)] = s[i] + ans;
		n++;
	}
	printf("\n");
}

int main() {
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		printf("Case #%d:", i);
		solve();
	}
}
