#include <bits/stdc++.h>
using namespace std;

int cnt[26];

typedef pair<int, int> pii;

pii a[26];

bool is_valid(int *cnt, int n) {
	for (int i = 0; i < n; ++i) {
		a[i] = pii(cnt[i], i);
	}
	sort(a, a + n);
	reverse(a, a + n);
	int total = 0;
	for (int i = 0; i < n; ++i) {
		total += cnt[i];
	}
	if (a[0].first > total / 2) return false;
	return true;
}

int main(void) {


	int cases; scanf("%d", &cases);

	int cas = 0;


	while (cases--) {
		printf("Case #%d: ", ++cas);
		int n = 0;
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			scanf("%d", &cnt[i]);
		}
		while (true) {

			assert(is_valid(cnt, n));
			int total = 0;
			for (int i = 0; i < n; ++i) {
				a[i] = pii(cnt[i], i);
				total += cnt[i];
			}
			sort(a, a + n);
			reverse(a, a + n);
			if (a[0].first == a[1].first && total != 3) {
				cnt[a[0].second]--;
				cnt[a[1].second]--;
				printf("%c%c", 'A'+a[0].second, 'A' + a[1].second);
			} else {
				--cnt[a[0].second];
				printf("%c", 'A' + a[0].second);
			}

			for (int i = 0; i < n; ++i) a[i] = pii(cnt[i], i);
			sort(a, a + n);
			reverse(a, a + n);
			if (a[0].first == 0) {
				puts("");
				break;
			} else {
				printf(" ");
			}
		}
	}

	return 0;
}