#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <cassert>
using namespace std;

const int INF = (int)1e9;

void solve(int test)
{
	int n;
	scanf("%d", &n);
	vector<int> list(n);
	for (int i = 0; i < n; i++)
		scanf("%d", &list[i]);
	int max_val = *max_element(list.begin(), list.end());
	int ans = INF;
	for (int cur_val = 1; cur_val <= max_val; cur_val++)
	{
		int cur_ans = cur_val;
		for (int x : list)
			cur_ans += (x + cur_val - 1) / cur_val - 1;
		ans = min(ans, cur_ans);
	}
	printf("Case #%d: %d\n", test, ans);
}

int main(int argc, char **argv)
{
	assert(argc >= 0);
	char *file = argv[1];
	freopen(file, "r", stdin);
	
	int tests;
	scanf("%d", &tests);
	for (int i = 0; i < tests; i++)
		solve(i + 1);


	return 0;
}
