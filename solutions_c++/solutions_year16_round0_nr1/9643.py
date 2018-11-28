#include <stdio.h>
#include <algorithm>
#include <string.h>

using namespace std;

int solve(int n){
	bool dig[10]; memset(dig, false, sizeof dig);
	int numD = 0,aux, aux2;
	for(int i=1; i< 1000 && numD != 10; i++){
		aux2 = aux = n*i;

		while(aux > 0){
			if(!dig[aux%10]){numD++; dig[aux%10] = true;}
			aux /= 10;
		}

	}

	if(numD != 10) return -1;
	return aux2;
}

int main(){
	int t,n;

	scanf("%d", &t);
	for(int test=1; test <= t; test++){
		scanf("%d", &n);
		int sol = solve(n);
		if(sol == -1) printf("Case #%d: INSOMNIA\n", test);
		else printf("Case #%d: %d\n", test, sol);
	}

	return 0;
}