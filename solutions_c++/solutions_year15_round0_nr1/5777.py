#include <stdio.h>
#include <stdlib.h>
#include <algorithm>

int nshyness[2000];

int main(){
	int T, indl;
	int n, i,total, ad;
	char c;
	FILE * ent;
	FILE * saida;
	ent = fopen("entrada1.txt", "r");
	saida = fopen("saida1.txt", "w");
	fscanf(ent, "%d", &T);
	for(indl=1; indl<=T; indl++){
		fscanf(ent, "%d", &n);
		for(i=0; i<=n; i++){
			fscanf(ent, " %c", &c);
			nshyness[i] = c-'0';
		}
		total=nshyness[0];
		ad=0;
		for(i=1; i<=n; i++){
			if(total<i){
				ad+=(i-total);
				total = i;
			}
			total +=nshyness[i];

		}
		fprintf(saida, "Case #%d: %d\n", indl, ad);
		//system("pause");

	}
}