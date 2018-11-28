#include <iostream>
#include <stdio.h>

using namespace std;

int main(int argc, char const *argv[])
{
	int t, ans, n, count;
	char A[1005];
	cin >> t;
	for (int zz = 1; zz <= t; zz++) {
		scanf("%d %s", &n, A);
		count = (int)A[0] - '0';
		ans = 0;
		for (int i = 1; i <= n; i++) {
			if (i > count) {
				ans += i - count;
				count += i - count;
			}
			count += (int)A[i] - '0';
		}
		printf("Case #%d: %d\n", zz, ans);
	}
	return 0;
}