#include <stdio.h>

int main(){
	int n, cont, k, casos, digitos;
	bool algarismos[10];
	scanf("%d", &casos);
	for (int c = 1; c <= casos; c++){
		scanf("%d", &n);
		if (n == 0)
			printf("Case #%d: INSOMNIA\n", c);
		else {
			digitos = 0;
			cont = 1;
			for (int i = 0; i < 10; i++)
				algarismos[i] = false;
			while (digitos != 10){
				k = cont * n;
				while (k > 0 && digitos != 10){
					if (!algarismos[k % 10]){
						algarismos[k % 10] = true;
						digitos++;
					}
					k = k / 10;
				}
				cont++;
			}
			printf("Case #%d: %d\n", c, (cont - 1) * n);
		}
	}
	return 0;
}