#include <stdio.h>
#include <math.h>

unsigned long long numBase(int *num, int n, int base){
	unsigned long long x = 0;
	for(int i = 0; i < n; i++){
		x = x * base;
		x += num[i];
	}
	return x;
}

unsigned long long divisor(long long num){
	unsigned long long i;
	if (num % 2 == 0)
		return 2;
	for (i = 3; i < sqrt(num) + 1; i += 2){
		if (num % i == 0)
			return i;
	}
	return -1;
}

int main(){
	int n, quant, casos, num[40];
	bool divisivel;
	unsigned long long x, divi, divisores[11];
	scanf("%d", &casos);
	for (int c = 1; c <= casos; c++){
		scanf("%d %d", &n, &quant);
		printf("Case #%d:\n", c);
		num[0] = 1;
		num[n - 1] = 1;
		for (int i = 1; i < n - 1; i++)
			num[i] = 0;
		for (int k = 1; k <= quant;){
			divisivel = true;
			for (int i = 2; i <= 10 && divisivel; i++){
				x = numBase(num, n, i);
				//printf("base %d - %llu\n", i, x);
				divi = divisor(x);
				if (divi != -1)
					divisores[i] = divi;
				else
					divisivel = false;
				//printf("divi %llu\n", divi);
			}
			if (divisivel){
				for (int i = 0; i < n; i++)
					printf("%d", num[i]);
				for (int i = 2; i <= 10; i++)
					printf(" %llu", divisores[i]);
				printf("\n");
				k++;
			}
			for (int i = n - 2, carry = 1; i > 0 && carry != 0; i--){
				if (carry = 1){
					num[i]++;
					carry = 0;
				}
				if (num[i] > 1){
					num[i] = 0;
					carry = 1;
				}
			}
		}
	}
	return 0;
}