#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
int TestCase, X, Y, R[20], C[20];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &TestCase);
	for (int Case = 1; Case <= TestCase; Case ++) {
		scanf("%d", &X);
		for (int i = 1, x; i <= 4; i ++) {
			for (int j = 1; j <= 4; j ++) {
				scanf("%d", &x);
				R[x] = i;
			}
		}
		scanf("%d", &Y);
		for (int i = 1, x; i <= 4; i ++) {
			for (int j = 1; j <= 4; j ++) {
				scanf("%d", &x);
				C[x] = i;
			}
		}
		int Ret = -1, Cnt = 0;
		for (int i = 1; i <= 16; i ++)
		if ((R[i] == X) && (C[i] == Y)) {
			Ret = i;
			Cnt ++;
		}
		printf("Case #%d: ", Case);
		if (Cnt == 1) {
			printf("%d\n", Ret);
		} else if (Cnt == 0) {
			printf("Volunteer cheated!\n");
		} else {
			printf("Bad magician!\n");
		}
	}
	return 0;
}
