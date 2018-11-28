#include <cstdio>

const int maxLength = 10000;

int n;
char tmp[maxLength + 1];

void testCase(int nr)
{
	scanf("%d%s", &n, tmp);
	int cnt = 0;
	int friends = 0;
	for (int i = 0; i <= n; ++i) {
		if (cnt < i) {
			++friends;
			++cnt;
		}
		cnt += tmp[i] - '0';
	}
	printf("Case #%d: %d\n", nr, friends);
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i)
		testCase(i);
}