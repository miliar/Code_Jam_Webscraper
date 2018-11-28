#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;

#define ll long long
#define INF 0x3f3f3f3f
#define LL_INF 0x3f3f3f3f3f3f3f3f
#define MAX

int main()
{
	//freopen("debug\\in.txt", "r", stdin);
	//freopen("CON", "w", stdout);
	int i, j, k;
	int test, kase = 1;
	scanf("%d", &test);
	while (test--) {
		int K, C, S;
		scanf("%d%d%d", &K, &C, &S);
		printf("Case #%d: ", kase++);
		ll length = 1;
		for (i = 1; i < C; ++i)
			length *= K;
		ll pos = 1;
		bool flag = 0;
		for (i = 1; i <= S; ++i) {
			if (!flag) flag = 1;
			else printf(" ");
			printf("%lld", pos);
			pos += length;
		}
		printf("\n");
	}
	return 0;
}