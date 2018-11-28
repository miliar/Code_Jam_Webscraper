#include <iostream>
#include <stdio.h>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <string.h>
#include <cmath>
#include <memory.h>
#include <algorithm>
using namespace std;
int n, x, v[10000];
int main()
{
	freopen("src.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int T = 1; T <= t; ++T){
		printf("Case #%d: ", T);
		scanf("%d%d", &n, &x);
		for (int i = 0; i < n; ++i)
			scanf("%d", v + i);
		sort(v, v + n);
		int res = 0;
		int l = 0, r = n - 1;
		while (l < r){
			if (v[l] + v[r] <= x){
				++res;
				++l;
				--r;
			}else{
				++res;
				--r;
			}
		}
		if (l == r)
			++res;
		printf("%d\n", res);
	}
	return 0;
}