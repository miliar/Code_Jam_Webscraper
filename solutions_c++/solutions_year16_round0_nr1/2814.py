#include <bits/stdc++.h>


int main(){
	int n;
	int cont=0;
	int vis[10], quant;
	long long int number;

	scanf("%d", &n);

	while(++cont <= n){
		quant=0;
		memset(vis,0,sizeof(vis));
		scanf("%lld", &number);
		if(number == 0){
			printf("Case #%d: INSOMNIA\n", cont);
			continue;
		}
		long long int c, x=1;

		while(quant < 10){
			c = number * x;
			//printf("   %lld\n", c);
			while(c > 0){
				int digit = c%10;
				c/=10;
				if(vis[digit] == 0){
					quant++;
				}
				vis[digit] = 1;
			}
			x++;
		}
		printf("Case #%d: %lld\n", cont, (x-1)*number);

	}



	return 0;
}