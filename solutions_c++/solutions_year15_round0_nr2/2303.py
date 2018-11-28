#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

#define MAXN 2000

int t, cas;
int mat[MAXN], n, x, mx;

int splitCost(int cakeNum, int limitNum) {
	if (cakeNum % limitNum == 0)
		return cakeNum / limitNum - 1;
	return cakeNum / limitNum;
}

int solve() {
	int ret = mx;
	for (int i = 1; i < mx; i++) {		//set the maximum plate
		int tmp = i;					//eating time
		for (int j = i + 1; j <= mx; j++)
			tmp += mat[j] * splitCost(j, i);	//arrange time
		ret = min(ret, tmp);
	}
	return ret;
}

int main() {
	scanf("%d", &t);
	for (cas = 1; cas <= t; cas++) {
		memset(mat, 0, sizeof mat);
		scanf("%d", &n);
		mx = 0;
		for (int i = 0; i < n; i++) {
			scanf("%d", &x);
			mat[x]++;
			mx = max(x, mx);
		}
		int ret = solve();
		printf("Case #%d: %d\n", cas, ret);
	}
	return 0;
}