#include <cstdio>
#include <cstring>

#define TOTAL 1000005
#define REP(i,n) for(__typeof(n) i=0; i<(n); i++)


typedef unsigned long long ull;

ull sol[TOTAL];


int test (int *bit) {


	REP(i,10)
		if (bit[i] == 0)
			return 0;

	return 1;

}


ull calcular(int i) {

	int continuar = 1;
	int bitset[10];

	ull N, N_tmp;
	int ind = 1;

	memset(bitset,0,sizeof bitset);


	while (continuar) {

		if (test(bitset))
			return N;

		N = i * ind;
		N_tmp = N;

		while (N_tmp != 0) {
			int cifra = N_tmp % 10;
			bitset[cifra] = 1;
			N_tmp/= 10;
		}
		ind++;
	}
}

void simulate () {

	sol[0] = 0;

	for (int i = 1; i < TOTAL; ++i) {
		sol[i] = calcular(i);
	}
}

void print () {


	REP(i,TOTAL)
		printf("%d => %llu\n",i,sol[i]);

} 

int main () {

	int TC;
	simulate();
	scanf("%d",&TC);

	int ind = 0;
	int numero;

//	print();

	while (TC--) {

		scanf("%d",&numero);
		printf("Case #%d: ",++ind);

		if (sol[numero] == 0)
			printf("INSOMNIA\n");
		else
			printf("%llu\n",sol[numero]);

	}
	
	return 0;
}