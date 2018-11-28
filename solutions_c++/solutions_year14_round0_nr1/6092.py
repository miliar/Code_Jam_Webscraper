// intento1.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <string>

using namespace std;

int main(int argc, char* argv[])
{
	int T;
	string nombre = "D:\\borrar\\A-small-attempt1.in";
	FILE *entrada = fopen(nombre.c_str(), "rt");
	nombre+=".out";
	FILE *salida = fopen(nombre.c_str(), "wt");
	fscanf(entrada,"%d", &T);
	for (int t=1;t<=T;t++) {
		int R;
		fscanf(entrada, "%d", &R);
		R-=1;
		char actual[17];
		for (int i=0;i<16;i++) {
			int k;
			fscanf(entrada, "%d", &k);
			if ((i/4)==R) {
				actual[k]=1;
			} else {
				actual[k]=0;
			}
		}
		fscanf(entrada, "%d", &R);
		R-=1;
		int posibles = 0;
		for (int i=0;i<16;i++) {
			int k;
			fscanf(entrada, "%d", &k);
			if ((i/4)==R) {
				if (actual[k]==1) {
					if (posibles != 0)
						posibles=-1;
					else
						posibles = k;
				}
			} 
		}
		if (posibles == 0) {
			fprintf(salida, "Case #%d: Volunteer cheated!\n", t); 
		} else if (posibles<0) {
			fprintf(salida, "Case #%d: Bad magician!\n", t);
		} else {
			fprintf(salida, "Case #%d: %d\n", t, posibles);
		}
	}
	fclose(salida);
	fclose(entrada);
	return 0;
}

