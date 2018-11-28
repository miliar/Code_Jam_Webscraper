#include <stdio.h>
#include <string>
#include <algorithm>
#include <stdlib.h>
#include <vector>
#include <iostream>
#define mod 1000000007
#define INT_MAX 2147483647
using namespace std;
int t, ans, n;
char str[105];
int main() {
	freopen("B-large.in", "r", stdin);
	freopen("bl.out", "w", stdout);
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++)
	{
		scanf("%s", str);
		n = strlen(str);
		ans = 0;
		for (int i = 1; i < n; i++)
			if (str[i] != str[i - 1])ans++;
		if (str[n - 1] == '-') ans++;
		printf("Case #%d: %d\n", tt, ans);
	}
	return 0;
}