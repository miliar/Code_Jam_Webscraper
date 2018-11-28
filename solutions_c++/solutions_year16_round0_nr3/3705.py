#include <bits/stdc++.h>
using namespace std;

FILE *in = fopen("f.in", "r");
FILE *out = fopen("f.out", "w");

int ntest, N, J;
vector<int> primes;
#define MAXP 111111111
bool notprime[MAXP];

int getdiv(int m, int b){
	long long num = 0, base = 1;
	for(int q = 0; q < N; q++){
		if(m & (1 << q)){
			num += base;
		}
		base *= b;
	}

	for(int p : primes){
		if(p >= num){
			break;
		}
		if(num % p == 0){
			return p;
		}
	}
	return -1;
}

int main(){
	memset(notprime, 0, sizeof notprime);
	for(int q = 2; q < MAXP; q++){
		if(!notprime[q]){
			primes.push_back(q);
			for(long long k = (long long)q * q; k < MAXP; k += q){
				notprime[k] = 1;
			}
		}
	}
	fprintf(out, "Case #1:\n");
	fscanf(in, "%d%d%d", &ntest, &N, &J);
	for(int q = 0; J && q < (1 << (N - 2)); q++){
		int m = (q << 1) | 1 | (1 << (N - 1));
		vector<int> divs;
		for(int b = 2; b <= 10; b++){
			int divisor = getdiv(m, b);
			if(divisor == -1){
				break;
			}
			divs.push_back(divisor);
		}
		if(divs.size() == 9){
			J --;
			for(int w = N - 1; w >= 0; w--){
				fprintf(out, "%d", (m & (1 << w)) ? 1 : 0);
			}
			for(int w : divs){
				fprintf(out, " %d", w);
			}
			fprintf(out, "\n");
		}
	}
	return 0;
}