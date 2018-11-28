#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <string.h>
#include <algorithm>    // std::sort
#include <vector>  
#include <math.h>
using namespace std;


int matriz[100][100];
int x[100], y[100];

bool resolve(int n, int m){
	int maximo=max(n,m);
	for(int i=0; i<maximo; i++){
		x[i]=0;
		y[i]=0;
	}

	for(int i=0; i<n; i++){
		for(int j=0; j<m; j++){
			if(matriz[i][j]==2){
				x[j]=2;
				y[i]=2;
			}
		}
	}

	for(int i=0; i<n; i++){
		for(int j=0; j<m; j++){
			if(matriz[i][j]==1 && x[j]==2 && y[i]==2){
				return false;
			}
		}
	}

	return true;

}


int main(){
	FILE *in = fopen("B-small-attempt0.in", "r");
	FILE *out = fopen("out.txt", "w");

	int t,n,m;
	fscanf(in, "%d", &t);

	for(int i=0; i<t; i++){
		fscanf(in, "%d%d", &n,&m);

		for(int j=0; j<n; j++){
			for(int k=0; k<m; k++){
				fscanf(in, "%d", &matriz[j][k]);
			}
		}


		if(resolve(n,m)){
			fprintf(out, "Case #%d: YES\n", i+1);
		}
		else{
			fprintf(out, "Case #%d: NO\n", i+1);
		}


	}

	
	return 0;
}


