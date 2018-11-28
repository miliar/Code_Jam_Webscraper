#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
using namespace std;

char buf[1005];
string s;

int amount[1005];
int n;

void stringToAmount () {
	for (int i = 0; i <= n; i++) {
		amount[i] = s[i] - '0';
	}
}

void solve ()
{
	stringToAmount();

	int ans = 0;
	int sum = 0;
	for (int i = 0; i <= n; i++) {
		if (amount[i] == 0)
			continue;

		if (sum < i) {
			ans += i - sum;
			sum = i;
		}
		sum += amount[i];
	}
	printf("%d", ans);
}

int main ()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int test_amount, test_num;

	scanf("%d\n", &test_amount);
	for (test_num = 0; test_num < test_amount; test_num++)
	{
		if (test_num)
			printf("\n");

		printf("Case #%d: ", test_num + 1);

		// input

		scanf("%d", &n);
		scanf("%s", buf);
		s = string(buf);

		// #input

		solve();
	}

	return 0;
}