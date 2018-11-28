#include <stdio.h>
#include <algorithm>
struct data {
	int chk, n;
	bool operator < (const data & l) const {
		return n < l.n;
	}
} d[1050];
int deck[1050];
int main() {
	freopen("B-large.in", "r", stdin);
	freopen("ans2_l.txt", "w", stdout);
	int T, test_no, n, i, j, k, st, en, ans;
	scanf("%d", &T);
	for(test_no = 1; test_no <= T; test_no++) {
		scanf("%d", &n);
		for(i = 1; i <= n; i++) {
			scanf("%d", &d[i].n);
			d[i].chk = i;
		}
		std::sort(d+1, d+n+1);
		for(i = 1; i <= n; i++) deck[d[i].chk] = i;
		st = 1, en = n, ans = 0;
		for(i = 1; i <= n; i++) {
			for(j = st; j <= en; j++) if(deck[j] == i) break;
			if(j-st < en-j) {
				ans += j-st;
				for(k = j-1; k >= st; k--) {
					deck[k+1] = deck[k];
				}
				st++;
			}
			else {
				ans += en-j;
				for(k = j+1; k <= en; k++) {
					deck[k-1] = deck[k];
				}
				en--;
			}
		}
		printf("Case #%d: %d\n", test_no, ans);
	}
	return 0;
}