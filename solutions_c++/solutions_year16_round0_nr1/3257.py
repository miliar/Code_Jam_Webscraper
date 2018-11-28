#include <iostream>


bool acabou (int count[]) {
	for (int i = 0; i <= 9; i++)
		if (count[i] == 0)
			return false;
	return true;
}
int main() {
	int t;
	scanf("%d ", &t);
	for (int tcase = 1; tcase <= t; tcase++) {
		long long int n;
		int count[12];
		for (int i = 0; i <= 9; i++)
			count[i] = 0;
		scanf("%lld ", &n);
		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", tcase);
			continue;
		}	
		long long int soma = 0;
		while(acabou(count) == false) {
			soma += n;
			long long int soma_copy = soma;
			while(soma_copy !=0 ) {
				int dig = soma_copy % 10;
				if (count[dig] == 0)
					count[dig] = 1;
				soma_copy /= 10;
			}
		}
		printf("Case #%d: %lld\n", tcase, soma);
		
	}
} 
