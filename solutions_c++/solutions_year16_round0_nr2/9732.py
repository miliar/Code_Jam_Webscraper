#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
#define sz(v) (int)v.size()

char str[101];

void clr (deque<char> &q) {
	while (sz(q) > 1 && q.back() == '+')
		q.pop_back();
	while (sz(q) >= 2 && q[0] == '+' && q[1] == '+')
		q.pop_front();
}

int calc (char a, char b) {
	if (a == '-' && b == '-') return 1;
	if (a == '-' && b == '+') return 1;
	if (a == '+' && b == '-') return 2;
	return 0;
}

int main ( ) {
	freopen("1", "rt", stdin);
	freopen("2", "wt", stdout);
	int tc, t = 0;
	scanf("%d", &tc);
	while (tc--) {
		scanf("%s", str);
		printf("Case #%d: ", ++t);
		deque<char> q;
		for (int i = 0; str[i]; i++)
			if (!sz(q) || q.back() != str[i]) q.push_back(str[i]);
		clr(q);
		int ans = 0;
		while (sz(q)) {
			clr(q);
			if (sz(q) == 0) break;
			else if (sz(q) == 1) {
				if (q[0] == '-') {
					ans++;
				}
				break;
			} else if (sz(q) == 2) {
				ans += calc(q[0], q[1]);
				q[0] = q[1] = '+';
				break;
			} else {
				if (q[0] == '+') {
					q[0] = '-';
					ans++;
				}
				reverse(q.begin(), q.begin() + sz(q));
				for (int i = 0; i < sz(q); i++)
					if (q[i] == '-') q[i] = '+';
					else q[i] = '-';
				ans++;
			}
		}
		printf("%d\n", ans);
	}
}
