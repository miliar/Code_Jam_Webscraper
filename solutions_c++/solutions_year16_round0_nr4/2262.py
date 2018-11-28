#include <iostream>
using namespace std;

int main()
{
	int t, k, c, s;
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);
	cin >> t;
	for (int times = 1; times <= t; times++) {
		cin >> k >> c >> s;
		printf("Case #%d:", times);
		for (int i = 1; i <= k; i++)
			printf(" %d", i);
		printf("\n");
	}
	return 0;
} 
