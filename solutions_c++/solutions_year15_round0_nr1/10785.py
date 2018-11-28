#include <cstdio>
#include <cstring>

#define MAX_S 2048

int main () {

    int TC;

    scanf("%d\n",&TC);
	int k = 0;
    while (TC--) {
		int S;
   		char cadena[MAX_S];
		scanf("%d %s\n",&S,cadena);
	
		int parados = 0;
		int invitados = 0;
		int t = strlen(cadena);
	
		int valor = cadena[0] - '0';
		parados+= valor;
	
		for (int i = 1; i < t; ++i) {
	    	valor = cadena[i] - '0';
			if (valor > 0) {
				if (parados < i) {
					int tmp = i - parados;
					invitados+= tmp;
					parados+= invitados;				
				}
				
				parados+= valor;
			}
		}

		printf("Case #%d: %d\n",++k,invitados);
	
    }

return 0;
}
