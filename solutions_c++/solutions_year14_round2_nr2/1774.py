#include <bits/stdc++.h>
using namespace std;

FILE * saida;

int main(int argc, char const *argv[]){
	//saida = stdout;
	saida = fopen("b.out", "w");
	int nc;
	cin >> nc;
	for(int caso = 1; caso <= nc; caso++){
		fprintf(saida, "Case #%d: ", caso);
		int a, b, k;
		cin >> a >> b >> k;
		int resp = 0;
		for(int i = 0; i < a; i++){
			for(int j = 0; j < b; j++){
				if((i&j) < k)
					resp++;
			}
		}
		fprintf(saida, "%d\n", resp);
	}
	fclose(saida);
	return 0;
}