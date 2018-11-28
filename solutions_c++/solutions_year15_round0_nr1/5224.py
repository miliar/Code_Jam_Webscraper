#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

int cnt[1024];
int T;
char buffer[1024];
int tot;
int maxlevel;
int ans;

int main()
{

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d\n", &T);

	tot = 0;
	ans = 0;

	while (T--) {
		scanf("%d %s\n", &maxlevel, buffer);
		tot++;
		ans = 0;
		memset(cnt, 0, sizeof(cnt));
		for (int i = 0; i <= maxlevel; i++) {
			cnt[i] = buffer[i] - '0';
		}

		for (int i = 1; i <= maxlevel; i++) {
			cnt[i] += cnt[i - 1];
		} 

		for (int i = 1; i <= maxlevel; i++) {
			if (cnt[i - 1] + ans < i) {
				ans += i - cnt[i - 1] - ans;
			}

		}
		printf("Case #%d: %d\n", tot, ans);

		
	}

	return 0;
}