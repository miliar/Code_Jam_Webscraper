#include <bits/stdc++.h>
using namespace std;

int cont = 0;
int TAM = 15;
long long digits;

void check(void);

void check(){
	vector<long long> divider;
	long long num;
	for(int base = 2; base <= 10; base++){
		num = 1 + pow(base, 15);
		for(int i = 1; i < 15; i++)
			if(digits & (1 << i))
				num += pow(base, i);

		bool dvsr = false;
		for(long long dvs = 3; dvs <= floor(sqrt(num)); dvs += 2)
			if(num % dvs == 0){
				//printf("numero = %lld, divisor = %lld\n", num, dvs);
				divider.push_back(dvs);
				dvsr = true;
				break;
			}
		if(!dvsr)
			return;
	}
	
	for(int i = 15; i >= 0; i--)
		printf("%d", (digits & (1 << i)) ? 1 : 0);
	for(int i = 0; i < 9; i++)
		printf(" %lld", divider[i]);
	printf("\n");
	cont++;
}

int main(){
	printf("Case #1:\n");
	digits = 1 | (1 << 15);
	for(; digits < (1 << 16); digits++){
		if(digits & 1)
			check();
		if(cont == 50)
			break;
	}
}