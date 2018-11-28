#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

typedef long long ll;

int t;
int k, c, s;

int main()
{
	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		scanf("%d %d %d", &k, &c, &s);
		ll mv = 1;
		for (int i = 0; i < c - 1; i++)
			mv *= ll(k);
		printf("Case #%d:", tc);
		ll cur = 1;
		for (int i = 0; i < s; i++) {
			printf(" %I64d", cur);
			cur += mv;
		}
		printf("\n");
	}
	return 0;
}