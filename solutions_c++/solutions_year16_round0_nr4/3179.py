#include<bits/stdc++.h>
using namespace std;

int main() {
	long long testes;
	scanf("%lld",&testes);
	int casos=1;
	while(testes-->0) {
		int K, C, S;
		scanf("%d %d %d", &K, &C, &S);
		printf("Case #%d:", casos++);
		for(int i=1; i<=K; i++){
			printf(" %d", i);
		}
		printf("\n");
	}
	return 0;
}