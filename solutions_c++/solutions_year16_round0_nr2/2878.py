#include <bits/stdc++.h>
long long int cont;
 
/* Driver program to test insertion sort */
int main()
{
    int n,c=0;
	scanf("%d", &n);
	char entrada[20000];
	while(++c <=n){
		cont = 0;
		scanf(" %s", entrada);
		int tam = strlen(entrada);
		int p = 0;

		while(p < tam){
			char first = entrada[0];
			p = 0;
			while(p<tam && entrada[p] == first){
				if(first == '-'){
					entrada[p] = '+';
				}else{
					entrada[p] = '-';
				}
				p++;
			}
			if(p == tam && first == '+'){
				break;
			}else{
				cont++;
			}
		}


		printf("Case #%d: %lld\n", c, cont);

	}
    return 0;
}