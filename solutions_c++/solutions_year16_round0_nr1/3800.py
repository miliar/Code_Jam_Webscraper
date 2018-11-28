#include<bits/stdc++.h>
using namespace std;

int main() {
	long long testes;
	scanf("%lld",&testes);
	int casos=1;
	while(testes --> 0) {
		long long N;
		scanf("%lld",&N);
		if(!N){
			printf("Case #%d: INSOMNIA\n", casos++);
			continue;
		}
		set<int>digits;
		long long aux = N;
		while(digits.size() < 10){
			long long aux_aux = aux;
			while(aux_aux){
				digits.insert(aux_aux%10);
				aux_aux/=10;
			}
			aux+=N;
		}
		printf("Case #%d:", casos++);
		printf(" %lld\n", aux-N);
	}
	return 0;
}