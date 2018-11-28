#include <iostream>
#include <cstdio>
using namespace std;
int vis[10];
void digit(int n) {
	while(n) {
		vis[n%10] = 1;
		n /= 10;
	}
}
bool check() {
	for(int i = 0 ; i < 10; i++) {
		if(!vis[i]) {
			return false;
		}
	}
	return true;
}
int main() {
	int n, t, cas = 0;
	scanf("%d",&t);
	while(t--) {
		memset(vis, 0, sizeof(vis));
		scanf("%d",&n);
		cas++;
		if(n == 0) {
			printf("Case #%d: INSOMNIA\n", cas);
			continue;
		}
		int count = 0;
		while(!check()) {
			count ++;
			digit(n*count);
		}
		printf("Case #%d: %d\n", cas, count*n);
	}
}