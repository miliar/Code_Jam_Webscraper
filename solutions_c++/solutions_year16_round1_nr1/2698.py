#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
#define sz(v) (int)v.size()

char str[1001];

int main ( ) {
	freopen("1", "rt", stdin);
	freopen("2", "wt", stdout);
	int tc, t = 0;
	scanf("%d", &tc);
	while (tc--) {
		scanf(" %s", str);
		deque<char> d;
		int n = strlen(str);
		for (int i = 0; i < n; i++) {
			if (!sz(d)) {
				d.push_back(str[i]);
				continue;
			}
			if (str[i] >= d.front()) d.push_front(str[i]);
			else d.push_back(str[i]);
		}
		printf("Case #%d: ", ++t);
		for (int i = 0; i < sz(d); i++)
			printf("%c", d[i]);
		printf("\n");
	}
	return 0;
}
