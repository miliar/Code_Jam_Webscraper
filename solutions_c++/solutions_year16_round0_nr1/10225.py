#include <stdio.h>
#include <string.h>

typedef long long int lld;

bool resp[11];

bool isFull(){
	for (int i =0 ; i < 10 ; i++){
		if (!resp[i]) return false;
	}
	return true;
}


bool make(lld n){
	lld i = 10, aux;
	aux = n;
	while (aux > 0 ){
		resp[aux%i] = true;
		aux = aux/i;
	}
	
	return isFull();
}

int main(){
	lld t, n;
	scanf("%lld", &t);
	
	for (lld caso = 1; caso <= t; caso++){
		scanf("%lld", &n);
		memset(resp, false, sizeof(resp));
		if (n == 0) {
			printf("Case #%lld: INSOMNIA\n", caso);
			continue;
		}
		lld i;
		
		for (i = 1; true; i++){
			if (make(n*i)) break;
		}
		
		printf("Case #%lld: %lld\n", caso, n*i);
	}
	
	
	return 0;
}
