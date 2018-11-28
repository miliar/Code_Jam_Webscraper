#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
struct aa {
	int zhi;
	int x, y;
};
bool cmp(struct aa a, struct aa b) {
	if (a.zhi > b.zhi)
		return true;
	return false;
}

void cheat(){
	int i;
	for(i=0;i<100;i++)
		i++;
}
int main() {
	int t;
	cin >> t;
	for (int iiii = 1; iiii <= t; iiii++) {
		int n, m;
		cin >> n >> m;
		int a[n][m];
		int hangmax[n], liemax[m];
		memset(hangmax, 0, sizeof(hangmax));
		memset(liemax, 0, sizeof(liemax));
		struct aa b[n * m];
		int i, j, k = 0;
		for (i = 0; i < n; i++)
			for (j = 0; j < m; j++) {
				cin >> a[i][j];
				if (a[i][j] > hangmax[i])
					hangmax[i] = a[i][j];
				if (a[i][j] > liemax[j])
					liemax[j] = a[i][j];
				b[k].x = i;
				b[k].y = j;
				b[k].zhi = a[i][j];
				k++;
			}
		sort(b, b + n * m, cmp);
		int flag = 0;
		int xx, yy, z;
		for (i = 0; i < n * m; i++) {
			xx = b[i].x;
			yy = b[i].y;
			z = b[i].zhi;
			if (z != hangmax[xx] && z != liemax[yy]) {
				flag = 1;
				break;
			}
		}
		printf("Case #%d: ", iiii);
		if (flag)
			printf("NO\n");
		else
			printf("YES\n");
	}
}
