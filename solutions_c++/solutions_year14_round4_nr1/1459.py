#include <cstdio>
#include <algorithm>

using std::sort;

const int maxN = 1000000;

int tmp[maxN];

int testCase()
{
	int n, limit;
	scanf("%d%d", &n, &limit);
	for (int i = 0; i < n; ++i) {
		scanf("%d", &tmp[i]);
	}
	sort(tmp, tmp + n);
	int left = 0, right = n - 1;
	int result = 0;
	while (left <= right) {
		if (tmp[left] + tmp[right] <= limit) {
			++left;
		}
		--right;
		++result;		
	}
	return result;
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		int result = testCase();
		printf("Case #%d: %d\n", i, result);
	}
}