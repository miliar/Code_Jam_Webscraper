#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <queue>
#include <stack>
#include <functional>

using namespace std;

int check[11];


int main()
{
	int T;
	char cake[111];
	scanf("%d", &T);
	for (int t = 1;t <= T;t++) {
		scanf("%s", cake);
		int ans = 0;
		int con;
		int now;
		int len = strlen(cake);
		if (cake[0] == '+') con = 1;
		else con = 0;
		for (int i = 1;i < len;i++) {
			if (cake[i] == '+') now = 1;
			else now = 0;
			if (now != con) {
				con = now;
				ans++;
			}
		}
		if (con == 0) ans++;
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}