#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

const int N = 10010;

int arr[N];

int main ()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout); 
	int T; scanf("%d", &T);
	for (int kase = 1; kase <= T; ++kase)
	{
		int n, x; scanf("%d %d", &n, &x);
		for (int i = 0; i < n; i++)
		{
			scanf("%d", &arr[i]);
		}
		sort(arr, arr + n);
		int ans = 0;
		for (int i = n - 1, j = 0; i >= j; i--)
		{
			++ans;
			if (i > j && arr[i] + arr[j] <= x) ++j;
		}
		printf("Case #%d: %d\n", kase, ans);
	}
	return 0;
}
