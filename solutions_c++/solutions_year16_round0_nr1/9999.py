#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main (void){
	int t, n, dig, cs = 1;
	ll aux;
	bool vis[10];
	scanf ("%d", &t);
	while (t--){
		scanf ("%d", &n);
		memset(vis,0,sizeof vis);
		
		if (n == 0)
			printf("Case #%d: INSOMNIA\n", cs++);
		else{	
			for (int i = 1, count = 0; count < 10; i++){
				aux = n * i;
				while (aux > 0){
					dig = aux % 10;
					if (!vis[dig]){
						vis[dig] = true;
						count ++;
					}
					aux = aux / 10;
				}	
				aux = n * i;			
			}
			printf("Case #%d: %lld\n", cs++, aux);
		}
	}
	
	return 0;
}
