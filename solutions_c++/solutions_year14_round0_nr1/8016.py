/*************************************************************************
    > File Name: a.cpp
    > Author: lax
    > Mail: xingkungao@gmail.com
    > Created Time: Sat 12 Apr 2014 09:25:01 PM CST
 ************************************************************************/

#include <iostream>
#include <cstdio>
using namespace std;
int t;
int A[4][4];
int B[4][4];
int p1, p2;
int ans;
int val;

int main() {
	int i, j;
	int kase = 0;
	scanf("%d", &t);
	while (kase++ < t) {
		scanf("%d", &p1);
		for (i = 0; i < 4; i++) 
			for (j = 0; j < 4; j++) 
				scanf("%d", &A[i][j]);
		scanf("%d", &p2);
		for (i = 0; i < 4; i++) 
			for (j = 0; j < 4; j++) 
				scanf("%d", &B[i][j]);
		ans = 0;
		val = 0 ;
		for (i = 0; i < 4; i++) {
			for (j = 0; j < 4; j++)  {
				if (A[p1-1][i] == B[p2-1][j]) {
					ans ++;
					val = A[p1-1][i];
				}
			}
		}
		if (ans == 0) 
			printf("Case #%d: Volunteer cheated!\n", kase);
		else if (ans == 1) 
			printf("Case #%d: %d\n", kase, val);
		else
			printf("Case #%d: Bad magician!\n", kase);

	}
	return 0;
}


