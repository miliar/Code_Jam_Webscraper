#include <stdio.h>
#include <math.h>
#include <string.h>

#define ull unsigned long long

int N, J;

void print2(ull n){
	if(n == 0){
		return;
	}
	print2(n/2);
	printf("%d", n%2);
}

bool is_prime(ull n){
	for(ull i=2; i*i<=n; i++){
		if(n%i == 0){
			return false;
		}
	}
	return true;
}

int main(void){

	int testcase;
	scanf("%d", &testcase);

	for(int t_itr=1; t_itr<=testcase; t_itr++){
		scanf("%d %d", &N, &J);

		printf("Case #%d:\n", t_itr);

		ull start = (1<<(N-1)) + 1;


		int jc = 0;
		for(; start < 1<<N; start += 2){
			
			ull s[11] = {};
			bool prime = false;
			for(int i=2; i<=10; i++){
				ull tmp = start;

				int c = 0;
				while(tmp > 0){
					s[i] += (tmp%2)*(ull)pow(i*1.0, c);
					tmp /= 2;
					c += 1;
				}
				if(is_prime(s[i])){
					prime = true;
					break;
				}
			}

			if(prime){
				continue;
			}

			print2(start);
			for(int i=2; i<=10; i++){
				
				for(ull j=2; j<s[i]; j++){
					if(s[i]%j == 0){
						s[i] /= j;
						break;
					}
				}
				
				printf(" %lld", s[i]);
			}
			printf("\n");

			jc += 1;
			if(jc == J){
				break;
			}
		}
	}

	return 0;
}