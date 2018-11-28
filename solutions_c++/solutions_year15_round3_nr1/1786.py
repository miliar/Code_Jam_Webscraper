#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	int R, C, W;
	int temp = 0;
	while (T--) {
		temp++;
		scanf("%d%d%d", &R, &C, &W);
		int ans = 0;
		if (C % W != 0) ans++;
		ans += C / W;
        ans += W - 1;
		printf("Case #%d: %d\n", temp, ans);;
	}
	return 0;
}
