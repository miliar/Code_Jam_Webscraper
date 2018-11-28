#include <stdio.h>
#define MAXN 110

int linha[MAXN], coluna[MAXN];
int m[MAXN][MAXN];
int alturasmaximas_l[MAXN];
int alturasmaximas_c[MAXN];

int maximo (int x, int y){
	if (x>y) return x;
	else return y;
}

int minimo(int x, int y){
	if (x<y) return x;
	else return y;
}

int max(int v[MAXN], int p, int q){
	if (q==p) return v[p];
	else{
		int m=(p+q)/2;
		return maximo(max(v, p, m), max(v, m+1, q));
	}
}

int main(){
	FILE * entrada; FILE * saida;
	entrada=fopen("entrada.txt", "r");
	saida=fopen("saida.txt", "w");
	int T;
	fscanf(entrada, "%d", &T);
	for (int t=0; t<T; t++){
		int M, N;
		fscanf(entrada, "%d %d", &M, &N);
		for (int i=0; i<M; i++){
			for (int j=0; j<N; j++)
				fscanf(entrada, "%d", &m[i][j]); 
		}
		for (int i=0; i<M; i++){
			for (int j=0; j<N; j++){
				linha[j]=m[i][j];				
			}
			alturasmaximas_l[i]=max(linha, 0, N-1);
		}
		for (int j=0; j<N; j++){
			for (int i=0; i<M; i++){
				coluna[i]=m[i][j];				
			}
			alturasmaximas_c[j]=max(coluna, 0, M-1);
		}
		bool ans=true;
		for (int i=0; i<M; i++){
			for(int j=0; j<N && ans; j++){
				if (minimo(alturasmaximas_l[i], alturasmaximas_c[j])!=m[i][j])
					ans=false;
			}
		}
		if (ans) fprintf(saida, "Case #%d: YES\n", t+1); 
		else fprintf(saida, "Case #%d: NO\n", t+1);
	}
}

