// Cookie Clicker Alpha.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <string>

using namespace std;

int main(int argc, char* argv[])
{
	int T;
	string nombre = "B-large.in";
	FILE *entrada = fopen(nombre.c_str(), "rt");
	nombre+=".out";
	FILE *salida = fopen(nombre.c_str(), "wt");
	fscanf(entrada,"%d", &T);
	for (int t=1;t<=T;t++) {
		double C, F, X;
		fscanf(entrada, "%lf", &C); 
		fscanf(entrada, "%lf", &F); 
		fscanf(entrada, "%lf", &X);
		//mejor inicial... no construir nada
		double R = X/2.0;
		double total = 0.0;
		double P=2.0;
		while (total<R) {
			//construir una mas
			total+=C/P;
			P+=F;
			double actual = total+(X/P);
			if (actual<R) {
				R=actual;
			}
		}
		fprintf(salida, "Case #%d: %0.08lf\n", t, R);
	}
	fclose(salida);
	fclose(entrada);
	return 0;
}

