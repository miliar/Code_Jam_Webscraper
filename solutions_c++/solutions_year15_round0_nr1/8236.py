#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <vector>
#include <set>
#include <map>
using namespace std;

const int MAXN = 1003;
int sm, sn[MAXN];
int sum[MAXN];
char buf[MAXN];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
	int T, Ca = 0; scanf("%d", &T);
	while (T--) {
		scanf("%d%s", &sm, buf);
		for (int i = 0; i <= sm; i++) sn[i] = buf[i] - '0';
		for (int i = 1; i <= sm; i++)
			sum[i] = sum[i - 1] + sn[i - 1];
		int ans = 0;
		for (int i = 1; i <= sm; i++)
		   ans = max(ans, i - sum[i]);
		printf("Case #%d: %d\n", ++Ca, ans);
	}
	return 0;
}
