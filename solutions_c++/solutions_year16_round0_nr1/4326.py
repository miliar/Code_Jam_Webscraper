#include <bits/stdc++.h>
using namespace std;

int getdig(int n){
	int m = 0;
	while(n){
		m |= (1 << (n % 10));
		n /= 10;
	}
	return m;
}

int main(){
	FILE *in = fopen("fl.in", "r");
	FILE *out = fopen("f.out", "w");
	int ntest;
	fscanf(in, "%d", &ntest);
	for(int test = 0; test < ntest; test++){
		int N;
		fscanf(in, "%d", &N);
		int baseN = N;
		int m = 0;
		if(N == 0){
			fprintf(out, "Case #%d: INSOMNIA\n", test + 1);
			continue;
		}
		while(m != (1 << 10) - 1){
			m |= getdig(N);
			N += baseN;
		}
		fprintf(out, "Case #%d: %d\n", test + 1, N - baseN);
	}
	return 0;
}