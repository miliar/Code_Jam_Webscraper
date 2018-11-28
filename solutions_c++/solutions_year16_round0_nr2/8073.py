#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <cstdio>
using namespace std;
#pragma warning(disable:4996)
int n, m;
int main() {
	int t;
	freopen("out.txt", "w", stdout);
	freopen("in.txt", "r", stdin);
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		int n;
		char str[1001];
		scanf("%s",  &str[1]);
		int ans = 0;
		int len = strlen(&str[1]); 
		bool min = false;
		for (int j = 1; j <= len; j++) {
			if (str[j] == '+' && !min) {
				if (j - 1 > 0)
					ans++;
				min = true;
			}
			else if (str[j] == '-' && min) {
				if (j - 1 > 0)
					ans++;
				min = false;
			}
		}
		if (!min)
			ans++;
		printf("Case #%d: %d\n", i,ans);
	}
	return 0;
}