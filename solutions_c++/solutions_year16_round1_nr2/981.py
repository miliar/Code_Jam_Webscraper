#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
int a[200][100], vis[3000], ans[100];

int main(){
	int T, kase = 0;
	freopen("Blarge.txt", "r", stdin);
	freopen("Blout.txt", "a", stdout);
	scanf("%d", &T);
	while(T--){
		int n;
		memset(vis, 0, sizeof(vis));
		scanf("%d", &n);
		for(int i = 0; i < 2*n-1; i++){
			for(int j = 0; j < n; j++){
				scanf("%d", &a[i][j]);
				vis[a[i][j]]++;
			}
		}
		printf("Case #%d: ", ++kase);
		int k = 0;
		for(int i = 1; i <= 2500; i++){
			if(vis[i] % 2){
				ans[k++] = i;
			}
		}
		for(int i = 0; i < k-1; i++){
			printf("%d ", ans[i]);
		}
		printf("%d\n", ans[k-1]);
	}
}
