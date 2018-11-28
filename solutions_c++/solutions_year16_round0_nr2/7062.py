#include <cstdio>
#include <iostream>
#include <set>

#define DEBUG 1

using namespace std;

void solve()
{
	int t, n;
	cin >> t;
	getchar();
	
	for (int it = 1; it <= t; ++it) {
		int ans = 0;
		char p = '\0', c;
		
		while ((c = getchar()) != '\n') {
			if (c == '-') {
				if (p == '\0') ans += 1;
				if (p == '+') ans += 2;
			}
			p = c;
		}
		
		printf("Case #%d: %d\n", it, ans);
	}
}

int main()
{
	
#ifdef DEBUG
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	
	solve();
	
	return 0;
}
