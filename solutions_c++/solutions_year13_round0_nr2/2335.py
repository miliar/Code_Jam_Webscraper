#include <stdio.h>
#include <string.h>

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t, m, n;
	int a[100][100];
	int cs, r1, r2, r3, t1, t2, t3;
	int cmax[100], rmax[100];
	bool flag;
	scanf("%d", &t);
	for(cs=1; cs<=t; cs++) {
		memset(cmax, 0, sizeof(cmax));
		memset(rmax, 0, sizeof(rmax));
		flag = true;
		scanf("%d %d", &n, &m);
		for(r1=0; r1<n; r1++) {
			for(r2=0; r2<m; r2++) {
				scanf("%d", &t1);
				a[r1][r2] = t1;
				if(t1 > rmax[r1]) {
					rmax[r1] = t1;
				}
				if(t1 > cmax[r2]) {
					cmax[r2] = t1;
				}
			}
		}
		for(r1=0; r1<n; r1++) {
			for(r2=0; r2<m; r2++) {
				t1 = a[r1][r2];
				if(t1 < rmax[r1] && t1 < cmax[r2]) {
					flag = false;
					break;
				}
			}
			if(flag == false) {
				break;
			}
		}
		if(flag == true) {
			printf("Case #%d: YES\n", cs);
		} else {
			printf("Case #%d: NO\n", cs);
		}
	}
	
}
