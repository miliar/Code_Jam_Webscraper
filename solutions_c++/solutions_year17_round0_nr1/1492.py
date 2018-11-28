#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
using namespace std;
char c[1020];
int n,m;
int main () {
	freopen("A-large.in", "r", stdin);
	freopen("data.out", "w", stdout);
	int T;
	cin >> T;
	for (int ii = 1; ii <= T; ++ii) {
		scanf("%s%d", c, &m);
		n = strlen(c);
		int ans = 0;
		for (int i = 0; i <= n-m ; ++i) {
			if (c[i] == '-') {
				ans++;
				for(int j = i; j < i+m ; ++j) {
					if(c[j] == '-') c[j] = '+';
					else c[j] = '-';
				}
			}
		}
		bool flag = true;
		for (int i = n-m+1; i < n; ++i)
			if (c[i] == '-') {
				flag = false;
				break;
			}
		printf("Case #%d: ", ii);
		if(flag) printf("%d\n", ans);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}