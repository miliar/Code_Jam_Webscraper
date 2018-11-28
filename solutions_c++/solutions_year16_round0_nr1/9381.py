#include <bits/stdc++.h>
using namespace std;

int go(int n) {
	int vis[11], aux=n, cnt=1;
	memset(vis, 0, sizeof(vis));
	while(1) {
		while(aux) {
			vis[aux%10]=1;
			aux/=10;
		}
		int f=0;
		for(int i=0; i<10; i++) if(!vis[i]) f=1;
		if(!f) return cnt*n;
		aux=(++cnt)*n;
	}
}

int main() {
	int T=1, t, n;
	scanf("%d", &t);
	while(t--) {
		scanf("%d", &n);
		printf("Case #%d: ", T++);
		if(!n) printf("INSOMNIA\n");
		else printf("%d\n", go(n));
	}
	return 0;
}
