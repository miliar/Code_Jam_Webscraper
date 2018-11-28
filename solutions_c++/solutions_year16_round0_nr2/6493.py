#include <bits/stdc++.h>
using namespace std;

#define endl "\n"
#define forn(i, n) for (int i = 0; i < n; ++i)
#define ford(i, n) for (int i = n - 1; i >= 0; --i)
#define fore(i, a, b) for (int i = a; i < b; ++i)
#define forl(i, x) for (int i = 0; i < x.size(); ++i)
const int MAXN = 105;
char s[MAXN];

void solve(int cas) {
	int res = 0;
	bool stt = true;
	int j = 0;
	ford(i, strlen(s)) {
		if ((s[i] == '-' && stt) || (s[i] == '+' && !stt)) {
			j = i;
			while (j >= 0 && s[j] == s[i]) {
				j--;
			}
			i = j + 1;
			stt = !stt; res++;
		}
	}
	printf("Case #%d: %d\n", cas, res);
}

int main() {
	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "wt", stdout);
	int t;
	scanf("%d", &t);
	getc(stdin);
	fore(i, 1, t + 1) {
		gets(s);
		solve(i);
	}
	return 0;
}