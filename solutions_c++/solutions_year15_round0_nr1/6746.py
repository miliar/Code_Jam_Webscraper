
#include <stdio.h>
#include <string.h>

int main(){
	int tcases;
	int Smax;
	char cadena[10009];
	scanf("%d", &tcases);

	for (int caseAct = 1 ; caseAct <= tcases; caseAct++ ){
		scanf("%d %s", &Smax, cadena);
		long long int mini = 0LL;
		long long int standing = 0LL;
		//printf("%d %s\n", Smax, cadena);
		for (int i = 0; i < strlen(cadena) ; i++){
			int hm = cadena[i] - '0';
			
			if (  standing + mini >= i  ){
				standing += hm;
			} else {
				mini += i - ( standing+ mini);
				standing += hm ;
			}
		}

		printf("Case #%d: %lld\n", caseAct, mini );
	}

	return 0;
}