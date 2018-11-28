#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int costo(vector<int> &A) {
    int total = 0;
    for (int i=0;i<A.size();i++) {
        int menor = A[i];
        int p = i;
        for (int j=i+1;j<A.size();j++) {
            if (menor>A[j]) {
                p=j;
                menor=A[j];
            }
        }
        for (int j=p;j>i;j--) {
            A[j] = A[j-1];
            total++;
        }
        A[i]=menor;
    }
    return total;
}

int minimo;
int N;
vector<int> A;

int convertir(vector<int> origen, vector<int> destino) {
    int res=0;
    for (int i=0;i<N;i++) {
        int j=i;
        while (origen[j]!=destino[i]) {
            j++;
        }
        while (j>i) {
            origen[j]=origen[j-1];
            res++;
            j--;
        }
        origen[i]=destino[i];
    }
    return res;
}

void busca(int indice,vector<int> B, vector<int> C) {
    if (indice == N) {
        sort(B.begin(),B.end());
        sort(C.begin(),C.end());
        for (int i=C.size()-1;i>=0;i--) {
            B.push_back(C[i]);
        }
        int actual = convertir(A,B);
        if (actual<minimo) {
            minimo=actual;
        }
        return;
    }
    vector<int> D = B, E = C;
    D.push_back(A[indice]);
    E.push_back(A[indice]);
    busca(indice+1,D,C);
    busca(indice+1,B,E);
}

int main(int argc, char* argv[])
{
	int T;
	#define NOMBRE_ARCHIVO "B-small-attempt1"
	string nombre = NOMBRE_ARCHIVO;
	nombre = nombre + ".in";
	FILE *entrada = fopen(nombre.c_str(), "rt");
	nombre = NOMBRE_ARCHIVO;
	nombre = nombre + ".out";
	FILE *salida = fopen(nombre.c_str(), "wt");
	fscanf(entrada,"%d", &T);
	for (int t=1;t<=T;t++) {
	    fscanf(entrada, "%d", &N);
	    A.resize(N);
        for (int i = 0; i < N; i++) {
            fscanf(entrada, "%d", &A[i]);
        }
        minimo = N*N;
        vector<int> vacio;
        vacio.resize(0);
        busca(0,vacio,vacio);
        fprintf(salida, "Case #%d: %d\n",t, minimo);
        printf("Case #%d: %d\n",t, minimo);
        fflush(salida);
		fflush(stdout);
	}
	fclose(salida);
	fclose(entrada);
	return 0;
}

