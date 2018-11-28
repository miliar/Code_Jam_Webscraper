#include <stdio.h>
#include <stdlib.h>

long double C, F, X;

long double f(long double n){
	if(n<0) n=0;
	long double sum = X/(2.0+n*F);
	int i;
	for(i=0; i<=n-1; i++)
		sum+=C/(2+i*F);
	return sum;
}

int main(){
	FILE * ent;
	FILE * saida;
	ent  = fopen("Cookie.txt", "r");
	saida = fopen("saida3.txt", "w");

	int T;
	fscanf(ent, "%d", &T);
	int cont;
	long double n;
	long double ans;
	int m;
	for(cont=0; cont < T; cont++){
		fscanf(ent, "%Lf %Lf %Lf", &C, &F, &X);
		printf("Lemos C, F, e D iguais a %Lf, %Lf e %Lf\n", C, F, X);
		m = X/C-2.0/F;
		n = m;
		ans = f(n);
		if(f(0)<ans) ans  = f(0);
		fprintf(saida, "Case #%d: %.8Lf\n", cont+1, ans);
	}
	system("pause");
}