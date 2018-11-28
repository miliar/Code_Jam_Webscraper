#include <cstdio>

int main(){
	//FILE * saida = fopen("cookie.out", "w");
	FILE * saida = stdout;
	int nc;
	scanf("%d", &nc);
	for(int caso = 1; caso <= nc; caso++){
		fprintf(saida, "Case #%d: ", caso);
		double c, f, x;
		scanf("%lf %lf %lf", &c, &f, &x);

		double taxa = 2;
		double total = 0;
		double restante = x/taxa;
		double restante_farm = (c/taxa) + x/(taxa + f);
		if(restante <= restante_farm)
			total = restante;
		else{
			while(restante > restante_farm){
				total += c/taxa;
				taxa += f;
				restante = x/taxa;
				restante_farm = (c/taxa) + x/(taxa + f);
			}
			total += x/taxa;
		}
		fprintf(saida, "%.7lf\n", total);
	}
	fclose(saida);
	return 0;
}