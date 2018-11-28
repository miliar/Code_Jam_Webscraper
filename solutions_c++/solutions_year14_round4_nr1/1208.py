#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int a[10010];
bool vis[10010];

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("b.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int t = 0; t < T; t++){
		int n, val;
		scanf("%d %d", &n, &val);
		for(int i = 0; i < n; i++) scanf("%d", &a[i]);
		sort(a, a + n);
		memset(vis, 0, sizeof(vis));
		int num = 0;
		for(int i = 0, j = n - 1; i <= j; i++){
			while(i < j && a[i] + a[j] > val){
				j--;
			}
			if(i < j){
				vis[j] = 1;
				j--;
			}
			else break;
		}
		for(int i = 0; i < n; i++) if(!vis[i]) num++;
		printf("Case #%d: %d\n", t + 1, num);
	}
    return 0;
}
