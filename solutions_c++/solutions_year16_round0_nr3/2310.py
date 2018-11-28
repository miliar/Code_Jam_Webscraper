#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <utility>
#include <cmath>

using namespace std;

int main(){
	int T;
	scanf("%d", &T);
	for (int test = 0; test < T; test++){
		unsigned N, J;
		scanf("%lu %lu", &N, &J);
		printf("Case #%d:\n", test + 1);
		/*
		// With Math, found 110 is the important suffix

		for (int i = 0; i < J; i++){
			for (int j = 0; j < N - 3; j++)
				if (i & (1 << j))
					printf("1");
				else
					printf("0");
			printf("110");
			for (int j = 2; j <= 10; j++)
				printf(" %d", j);
			printf("\n");
		}*/
		unsigned long long count = 0;
		while (J){
			unsigned long long state = (1 << (N - 1)) | (count << 1) | 1;
			bool ok = true;
			int divisor[9];
			for (int base = 2; base <= 10; base++){
				unsigned long long sum = 0, mult = 1;
				for (int i = 0; i < N; i++){
					if (state & (1 << i))
						sum += mult;
					mult *= base;
				}
				bool comp = false;
				for (int i = 2; i < sqrt(sum); i++)
					if (sum % i == 0){
						comp = true;
						divisor[base - 2] = i;
						break;
					}
				if (!comp){
					ok = false;
					break;	
				}
			}
			if (ok){
				for (int i = N - 1; i >= 0; i--)
					if (state & (1 << i))
						printf("1");
					else
						printf("0");
				for (int i = 0; i < 9; i++)
					printf(" %d", divisor[i]);
				printf("\n");
				J--;
			}
			count++;
		}
	}
}
