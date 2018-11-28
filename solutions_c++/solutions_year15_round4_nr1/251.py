#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>

#define fo(i,a,b) for(int i = a; i<=b; i++)
#define fox(i,a,b) for(int i = a; i>=b; i--)
using namespace std;

char a[200][200];
int b[200][200];
int c[200][200];
int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T;
	scanf("%d", &T);
	int n,m;
	for (int t = 1; t <= T; t++){
		scanf("%d %d\n",&n, &m);
		fo(i,1,n) {
			fo(j,1,m){
				scanf("%c", &a[i][j]);
				b[i][j] = 0;
				c[i][j] = 0;
			}
			scanf("\n");
		}
		int ans = 0;
		fo(i,1,n) fo(j,1,m){
			if (a[i][j] == '^'){
				int flag = 0;
				fox(ii,i - 1,1)
					if (a[ii][j] != '.'){
						b[ii][j] = 1;
						flag = 1;
						break;
					}
				if (flag == 0) {
					ans++;
					c[i][j] = 1;
				}
			}
			if (a[i][j] == 'v'){
				int flag = 0;
				fo(ii,i + 1,n)
					if (a[ii][j] != '.'){
						b[ii][j] = 1;
						flag = 1;
						break;
					}
				if (flag == 0) {
					ans++;
					c[i][j] = 1;
				}
			}
			if (a[i][j] == '<'){
				int flag = 0;
				fox(jj,j - 1,1)
					if (a[i][jj] != '.'){
						b[i][jj] = 1;
						flag = 1;
						break;
					}
				if (flag == 0) {
					ans++;
					c[i][j] = 1;
				}
			}
			if (a[i][j] == '>'){
				int flag = 0;
				fo(jj,j + 1,m)
					if (a[i][jj] != '.'){
						b[i][jj] = 1;
						flag = 1;
						break;
					}
				if (flag == 0) {
					ans++;
					c[i][j] = 1;
				}
			}
		}
		fo(i,1,n) fo(j,1,m){
			if (a[i][j] != '.' && b[i][j] == 0 && c[i][j] == 1){
				int flag = 0;
				fo(ii,1,n)
					if (a[ii][j] != '.' && ii != i) {
						flag = 1;
						break;
					}
				fo(jj,1,m)
					if (a[i][jj] != '.' && jj != j) {
						flag = 1;
						break;
					}
				if (!flag){
					ans = -1;
					break;
				}
			}
		}
		printf("Case #%d: ", t);
		if (ans != -1)
			printf("%d\n", ans);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}
