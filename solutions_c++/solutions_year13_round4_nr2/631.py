#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
#include <iostream>
#include <stack>

using namespace std;

int arr[11][10000];
bool was[10000];
int sz = 0;
int n, p;

void rec(int a, int b, int dep)
{
	if(dep == n + 1)
		return;
	int cer = (a + b) / 2 + 1;
	for(int i = a, j = 0; i < b; i+=2, j ++)
	{
		arr[dep][a + j] = min(arr[dep - 1][i + 1], arr[dep - 1][i]);
		arr[dep][cer + j] = max(arr[dep - 1][i + 1], arr[dep - 1][i]);
	}
	rec(a, cer - 1, dep + 1);
	rec(cer, b, dep + 1);
}

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int t;
	scanf("%d", &t);
	for(int tt = 0; tt < t; tt++)
	{
		scanf("%d%d", &n, &p);

		sz = (1 << n);
		for(int i = 0; i < sz; i++)
			arr[0][i] = i;
		bool id = 0;
		rec(0, sz - 1, 1);
		int ma = 0;
		for(int i = 0; i < p; i++)
			ma = max(ma, arr[n][i]);
		int mi = 0;
		memset(was, 0, sizeof(was));
		for(int i = 0; i < p; i++)
			was[arr[n][i]] = 1;
		for(; was[mi]; mi++);
		printf("Case #%d: %d %d\n", tt + 1, mi - 1, ma);
	}

	return 0;
}