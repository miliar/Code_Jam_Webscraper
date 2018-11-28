#include <bits/stdc++.h>
using namespace std;

int cnt[10];

bool complete(){
	for(int i = 0; i <= 9; i++){
		if(cnt[i] == 0) return false;
	}
	return true;
}

int main(void){
	int t;
	scanf("%d", &t);

	for(int k = 1; k <= t; k++){
		memset(cnt, 0, sizeof cnt);
		long long n, times = 1LL;
		scanf("%lld", &n);
		if(n == 0){
			printf("Case #%d: INSOMNIA\n", k);
		}
		else{
			long long nn = n;
			while(1){
				long long aux = nn;
				while(aux != 0){
					int digit = aux%10;
					cnt[digit]++;
					aux /= 10;
				}
				if(complete()) break;
				nn = n*(++times);
			}

			printf("Case #%d: %lld\n", k, nn);
		}	
	}

	return 0;
}
