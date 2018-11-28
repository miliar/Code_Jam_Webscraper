#include <bits/stdc++.h>
using namespace std;

bool check(char * entrada, int tam){
	for(int i = 0; i < tam; i++)
		if(entrada[i] == '-')
			return false;
	return true;
}

int main(){
	int casos;
	cin >> casos;

	for(int caso = 1; caso <= casos; caso++){
		printf("Case #%d: ", caso);

		char entrada[110];
		int tam;
		scanf("%s", entrada);
		tam = strlen(entrada);

		int cont = 0;
		while(!check(entrada, tam)){
			if(entrada[0] == '+'){
				int i = 0;
				do{
					entrada[i] = '-';
					i++;
				}while(i < tam && entrada[i] == '+');
			}
			else{
				int i = 0;
				do{
					entrada[i] = '+';
					i++;
				}while(i < tam && entrada[i] == '-');
			}
			cont++;
		}

		printf("%d\n", cont);
	}
}