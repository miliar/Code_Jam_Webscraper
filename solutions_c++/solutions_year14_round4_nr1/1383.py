#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char* argv[])
{
	int T;
	#define NOMBRE_ARCHIVO "A-large"
	string nombre = NOMBRE_ARCHIVO;
	nombre = nombre + ".in";
	FILE *entrada = fopen(nombre.c_str(), "rt");
	nombre = NOMBRE_ARCHIVO;
	nombre = nombre + ".out";
	FILE *salida = fopen(nombre.c_str(), "wt");
	fscanf(entrada,"%d", &T);
	for (int t=1;t<=T;t++) {
	    int N,X;
	    vector<int> S;
	    fscanf(entrada, "%d", &N);
	    fscanf(entrada, "%d", &X);
	    S.resize(N);
        for (int i = 0; i < N; i++) {
            fscanf(entrada, "%d", &S[i]);
        }
        sort(S.begin(),S.end());
        int total = 0;
        int a = 0;
        int b = S.size()-1;
        while (a<b) {
            if ((S[a]+S[b])>X) {
                b--;
            } else {
                b--;
                a++;
            }
            total++;
        }
        if (a==b) {
            total++;
        }
        fprintf(salida, "Case #%d: %d\n",t, total);
        printf("Case #%d: %d\n",t, total);
        fflush(salida);
		fflush(stdout);
	}
	fclose(salida);
	fclose(entrada);
	return 0;
}

