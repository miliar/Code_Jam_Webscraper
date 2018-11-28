#include <set>
#include <map>
#include <cmath>
#include <cstdio>
#include <vector>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

int cas, n, m, k;
int a[5][5], b[5][5];

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d", &cas);
	for (int t = 1; t <= cas; t++) {
		scanf("%d", &n);
		for (int i = 1; i < 5; i++)
			for (int j = 1; j < 5; j++) scanf("%d", &a[i][j]);
		scanf("%d", &m);
		for (int i = 1; i < 5; i++)
			for (int j = 1; j < 5; j++) scanf("%d", &b[i][j]);
		k = 0;
		for (int i = 1; i < 5; i++) {
			for (int j = 1; j < 5; j++) 
				if (a[n][i] == b[m][j]) {
					if (k == 0) k = i; else k = 5;
					break;
				}
		}
		printf("Case #%d: ", t);
		if (k == 0) 
			puts("Volunteer cheated!");
		else if (k == 5)
			puts("Bad magician!");
		else 
			printf("%d\n", a[n][k]);

	}
	return 0;
}

