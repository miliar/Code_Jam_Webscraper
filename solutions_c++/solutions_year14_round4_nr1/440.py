#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string.h>
#include <string>
#include <math.h>
#include <vector>
using namespace std;

const int maxn = 100000 + 10;
int a[maxn], n, m;
bool mark[maxn];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A_large.out", "w", stdout);
	int TextN;
	scanf("%d", &TextN);
	for (int TT = 1; TT <= TextN; TT++) {
		scanf("%d%d", &n, &m);
		for (int i = 1; i <= n; i++) scanf("%d", a + i);
		sort(a + 1, a + 1 + n);
		memset(mark, 0, sizeof(mark));
		int ans = 0;
		for (int i = n; i >= 1; i--) 
		if (!mark[i]) {
			int k = 0;
			for (int j = i-1; j >= 1; j--)
				if (!mark[j] && a[i]+a[j] <= m) {
					k = j;
					break;
				}
			mark[k] = true;
			++ans;
		}
		printf("Case #%d: %d\n", TT, ans);

	}
}