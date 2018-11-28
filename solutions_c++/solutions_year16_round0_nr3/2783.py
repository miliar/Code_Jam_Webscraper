#include <iostream>
using namespace std;

void soma2(int num[]) {
	int carry;
	int dig = 1;
	do {
		num[dig] ^= 1;
		if (num[dig] == 0)
			carry = 1;
		else 
			carry = 0;
		dig++;
	}   while(carry == 1);
}

long long int converte(int num[], int len, int base) {
	long long int soma = 0;
	long long int fator = 1;
	for (int i = 0; i < len; i++) {
		soma += num[i] * fator;
		fator *= base;
	}
	return soma;
}

long long int divisor(long long int n) {
	for (long long int i = 2; i * i <= n; i++)
		if (n % i == 0)
			return i;
	return 0; // é primo
}

int main() {
	int t;
	scanf("%d ", &t);
	for (int tcase = 1; tcase <= t; tcase++) {
		int n, j;
		scanf("%d %d ", &n, &j);
		int num[34];
		num[0] = num[n - 1] = 1;
		for (int i = 1; i < n - 1; i++)
			num[i] = 0;
		
		int qtd = 0;
		printf("Case #%d:\n", tcase);
		while(qtd < j) {
			long long int div[15];
			for (int base = 2; base <= 10; base++) {
				long long int convertido = converte(num, n, base);
				div[base] = divisor(convertido);
			}
			bool serve = true;
			for (int i = 2; i <= 10; i++)
				if (div[i] == 0) {
					serve = false;
					break;
				}
			if(serve) {
				for (int i = n - 1; i >= 0; i--)
					printf("%d", num[i]);
				printf(" ");
				for (int i = 2; i <= 10; i++)
					printf("%lld ", div[i]);
				printf("\n");
				qtd++;
			}
			soma2(num);
		}
		
		
	}
	return 0;
}
