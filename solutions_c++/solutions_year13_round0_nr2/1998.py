#include <cstdio>
#include <algorithm>

using namespace std;

int a[100][100];
int rowmax[100], colmax[100];

int main() {
	int T;
	scanf(" %d", &T);
	for(int t = 0; t < T; t ++) {
		int n, m;
		scanf(" %d %d", &n, &m);
		for(int i = 0; i < 100; i ++)
			rowmax[i] = 0, colmax[i] = 0;
		for(int i = 0; i < n; i ++)
			for(int j = 0; j < m; j ++) {
				scanf(" %d", &a[i][j]);
				rowmax[i] = max(rowmax[i], a[i][j]);
				colmax[j] = max(colmax[j], a[i][j]);
			}
		bool poss = true;
		for(int i = 0; i < n; i ++)
			for(int j = 0; j < m; j ++)
				poss &= ((a[i][j] == rowmax[i]) || (a[i][j] == colmax[j]));
		printf("Case #%d: ", t + 1);
		if(poss)
			printf("YES\n");
		else
			printf("NO\n");
	}
	return 0;
}
