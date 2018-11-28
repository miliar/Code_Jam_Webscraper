#include <stdio.h>
#define MAXN 1000

long long N=10000000;
long long todos_fair[MAXN];
long long digitos( long long n){
	long long pot=1, exp=0;
	while (pot<=n){
		pot*=10;
		exp++;
	}
	return exp;
}
long long primeiro_dig(long long n){
	long long pot=1;
	for (long long i=1; i<digitos(n); i++)
		pot*=10;
	for (int i=1; i<n; i++)
		if (i*pot>n) return i-1;
	return 10;
}
bool ispalind(long long n){
	if (n==0) return true;
	if (n==n%10) return true;
	if (primeiro_dig(n)!=n%10) return false;
	else{
		long long pot=1;
		for (long long i=1; i<digitos(n); i++)
			pot*=10;
		return ispalind((n-pot*(n%10))/10);
	}
}

int main(){
	int T;
	FILE *entrada; FILE * saida;
	entrada = fopen("entrada.txt", "r");
	saida = fopen("saida.txt", "w");
	fscanf (entrada, "%d", &T);
	printf("T vale %d.\n", T);
	long long fim =0;
	for (long long i=0; i<N; i++){
		long long square=i*i;
		if (ispalind(square)){
			if (ispalind(i)){
				todos_fair[fim]=square;
				fim++;
				printf("%lld eh palindromo-fair \n", square);
			}
			else printf("%lld eh palindromo not-fair \n", square);
		}
	}
	int x,y;
	for (int u=0; u<T; u++){
		fscanf(entrada, "%d", &x);
		fscanf(entrada, "%d", &y);
		int i=0;
		while (todos_fair[i]<x)
			i++;
		int j=i;
		while (todos_fair[j]<=y)
			j++;
		fprintf(saida, "Case #%d: %d\n", u+1, j-i);
	}
}
