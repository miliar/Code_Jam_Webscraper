#include <cstdio>
using namespace std;

int main() {
	int T;
	int ordenamiento[5], cont;
	int fila, carta;
	scanf("%d", &T);
	for(int i = 1; i <= T; i++){
		scanf("%d", &fila);
		for(int j = 1; j <= 4; j++)
			for(int k = 1, c; k <= 4; k++){
				scanf("%d", &c);
				if(fila == j)
					ordenamiento[k-1] = c;
			}
		cont = 0;
		scanf("%d", &fila);
		for(int j = 1; j <= 4; j++)
			for(int k = 1, c; k <= 4; k++){
				scanf("%d", &c);
				if(fila == j)
					for(int idx = 0; idx < 4; idx++)
						if(ordenamiento[idx] == c){
							cont++;
							carta = c;
						}
			}
			
		if(cont == 0)
			printf("Case #%d: Volunteer cheated!\n", i);
		else
			if(cont > 1)
				printf("Case #%d: Bad magician!\n", i);
			else printf("Case #%d: %d\n", i, carta);
			
	}
	return 0;
}