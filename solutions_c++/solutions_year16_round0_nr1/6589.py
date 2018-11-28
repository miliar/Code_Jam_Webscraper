#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
int vis[15];

int main(){
	int T, kase = 0;
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &T);
	while(T--){
		int n, cnt = 0;
		memset(vis, 0, sizeof(vis));
		scanf("%d", &n);
		printf("Case #%d: ", ++kase);
		if(n == 0){
			printf("INSOMNIA\n");
			continue;
		}
		for(int i = 1; ; i++){
			int t = i*n;
			while(t){
				int x = t%10;
				if(!vis[x]){
					vis[x] = 1;
					cnt++;
				}
				t /= 10;
			}
			if(cnt == 10){
				printf("%d\n", i*n);
				break;
			}
		}
	}
}
