#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>

using namespace std;

int t,maxn,n,m;
int a[111][111],b[111][111];
bool f;

int main(){

	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);

	scanf("%d", &t);
	for (int z = 1; z <= t; z++){
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++){
			for (int j = 0; j < m; j++){
				scanf("%d", &a[i][j]);
			}
		}
		f = true;
		for (int i = 0; i < n; i++){
			maxn = 0;
			for (int j = 0; j < m; j++){
				maxn = max(a[i][j], maxn);
			}
			for (int j = 0; j < m; j++){
				if (a[i][j] == maxn) b[i][j] = 1;
			}
		}
		for (int j = 0; j < m; j++){
			maxn = 0;
			for (int i = 0; i < n; i++){
				maxn = max(a[i][j], maxn);
			}
			for (int i = 0; i < n; i++){
				if (a[i][j] == maxn) b[i][j] = 1;
			}
		}
		for (int i = 0; i < n; i++){
			for (int j = 0; j < m; j++){
				if (b[i][j] == 0){
					f = false;
				}
				b[i][j] = 0;
			}
		}
		printf("Case #%d: ", z);
		if (f) printf("YES\n");
		else printf("NO\n");
	}
	return 0;

}
