#include <bits/stdc++.h>

using namespace std;
int t,tes,n,ans,i;
char s[100][100];

void DFS(int x, int y, int z) {
	if (y == n) {
		if (x == n-1) {
			bool valid = true;
			bool udah[10];
			map<int,int> mem;
			int i,j;
			
			for (j=0 ; j<n ; j++) udah[j] = false;
			for (i=0 ; i<=64 ; i++) mem[i] = 0;
			for (i=0 ; i<n ; i++) {
				int x = 0;
				for (j=0 ; j<n ; j++) {
					x += (1 << j) * (s[i][j] - '0');
					if (s[i][j] == '1') udah[j] = true;
				}
				mem[x]++;
			}
			for (j=0 ; j<n ; j++) if (!udah[j]) valid = false;
			int y = 0;
			for (i=0 ; i<=64 ; i++) if (mem[i] > 0) {
				int zz = __builtin_popcount(i);
				if (zz != mem[i]) valid = false;
				y += zz;
			}
			if (y != n) valid = false;
			if (valid) ans = min(ans,z);
		} else {
			DFS(x+1,0,z);
		}
	} else {
		if (s[x][y] == '1') {
			DFS(x,y+1,z);
		} else {
			DFS(x,y+1,z);
			s[x][y] = '1';
			DFS(x,y+1,z+1);
			s[x][y] = '0';
		}
	}
}

int main() {
	scanf("%d",&t);
	for (tes=1 ; tes<=t ; tes++) {
		scanf("%d",&n);
		for (i=0 ; i<n ; i++) scanf("%s",s[i]);
		ans = 9999999;
		DFS(0,0,0);
		printf("Case #%d: %d\n",tes,ans);
	}
}