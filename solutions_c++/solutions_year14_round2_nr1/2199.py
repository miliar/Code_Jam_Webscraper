#include <cstdio>
#include <vector>
#include <cstring>
#include <algorithm>

using namespace std;

#define REP(x, n) for (int x = 0; x < n; ++x)
#define FOR(x, b, e) for (int x = b; x <= (e); ++x)

const int MAX = 110;
const int BARZYLION = 2e9;

char str[MAX];
int tab[MAX][MAX], n;

void clear() {
	REP(i, MAX) {
		str[i] = 0;
		
		REP(j, MAX) {
			tab[i][j] = 0;
		}
	}
}

bool check(int id, bool first = false) {
	int len, charId;
	char tmp[MAX];

	scanf("%s", tmp);

	len = strlen(tmp);

	charId = -1;
	REP(i, len) {
		if (i == 0 || tmp[i] != tmp[i-1]) {
			charId++;
			if (first) {
				str[charId] = tmp[i];
			} else if (str[charId] != tmp[i]) {
				return false;
			}
		}
		tab[id][charId]++;
	}
	if (str[charId+1] != 0) return false;

	return true;
}

int sum(int id, int target) {
	int res = 0;
	REP(i, n) {
		res += abs(tab[i][id] - target);
	}

	return res;
}

int best(int id) {
	int maxx = -1, res = BARZYLION;

	REP(i, n) {
		maxx = max(maxx, tab[i][id]);
	}

	FOR(i, 1, maxx) {
		res = min(res, sum(id, i));
	}

	return res;
}

int solve() {
	int res = 0;

	scanf("%d", &n);

	clear();

	REP(i, n) {
		if (i == 0) check(i, true);
		else if (!check(i)) return -1;
	}

	int len = 0;
	while (tab[0][len] != 0) {
		len++;
	}

	REP(i, len) {
		res += best(i);
	}

	return res;
}

int main() {
	int t;

	scanf("%d", &t);
	FOR(q, 1, t) {
		int res = solve();
		
		printf("Case #%d: ", q);
		if (res == -1) {
			printf("Fegla Won");
		} else {
			printf("%d", res);
		}
		printf("\n");
	}

	return 0;
}
