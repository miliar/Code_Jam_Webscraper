#include <stdio.h>
#include <math.h>

int main(){
	FILE * entrada; FILE * saida;
	entrada=fopen("entrada.txt", "r");
	saida=fopen("saida.txt", "w");
	int T;
	fscanf(entrada, "%d", &T);
	for (int u=0; u<T; u++){
		long double r, n;
		fscanf(entrada, "%Lf %Lf", &r, &n);
		long double m=sqrt(8*n+(2*r-1)*(2*r-1));
		m=floor(m);
		long double ans=floor((m-2*r+1)/4.0);
		fprintf(saida, "Case #%d: %.0Lf\n", u+1, ans);
	}
	fclose(entrada);
	fclose(saida);
	return 0;
}