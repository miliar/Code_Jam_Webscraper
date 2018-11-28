#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

int T;
int r, c, w;

int main() {
	scanf("%d", &T);

	for(int t = 1; t <= T; t++) {
		scanf("%d%d%d", &r, &c, &w);

		int ans = 0;
		ans = r * c / w;
		ans += w - 1;
		if(c % w != 0)
			ans++;
		
		printf("Case #%d: %d\n", t, ans);
	}

	return 0;
}