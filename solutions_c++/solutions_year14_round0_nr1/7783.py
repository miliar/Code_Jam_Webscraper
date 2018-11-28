/*************************************************************************
    > File Name: codejamA.cpp
    > Author: skt
    > Mail: sktsxy@gmail.com 
    > Created Time: 2014年04月12日 星期六 21时12分19秒
 ************************************************************************/

#include<bits/stdc++.h>
using namespace std;
#define MAXN 5
int t, Cas = 1, a[MAXN][MAXN], b[MAXN][MAXN], r1, r2, cnt, now;
void work()
{
	scanf("%d", &r1);
	for (int i = 1; i <= 4; i ++) {
		for (int j = 1; j <= 4; j ++) {
			scanf("%d", &a[i][j]);
		}
	}
	scanf("%d", &r2);
	for (int i = 1; i <= 4; i ++) {
		for (int j = 1; j <= 4; j ++) {
			scanf("%d", &b[i][j]);
		}
	}
	cnt = 0;
	for (int i = 1; i <= 4; i ++) {
		for (int j = 1; j <= 4; j ++) {
			if (a[r1][i] == b[r2][j]) {
				cnt ++;
				now = a[r1][i];
			}
		}
	}
	printf("Case #%d: ", Cas ++);
	if (cnt == 1) {
		printf("%d\n", now);
	} else if (cnt != 0) {
		printf("Bad magician!\n");
	} else {
		printf("Volunteer cheated!\n");
	}
}
int main()
{
	scanf("%d", &t);
	while (t --) {
		work();
	}
	return 0;
}
