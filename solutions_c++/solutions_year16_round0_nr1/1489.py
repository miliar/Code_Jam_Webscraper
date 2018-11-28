#include <cstdio>
#include <set>

int main(void) {
	int t;
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		int tmp;
		scanf("%d", &tmp);
		if (tmp == 0)
		{
			printf("Case #%d: INSOMNIA\n", i);
			continue;
		}
		std::set<int> con;
		int ans;
		for (int j = tmp; ; j += tmp) {
			int tmp = j;
			while (tmp != 0) {
				con.insert(tmp % 10);
				tmp /= 10;
			}
			if (con.size() == 10) {
				ans = j;
				break;
			}
		}
		printf("Case #%d: %d\n", i, ans);
	}
}