#include <cstdio>

using namespace std;

int calcular(int a, int b, int c){
	int i, j, cont = 0;

	for(i = 0; i < a; i++){
		for(j = 0; j < b; j++){
			int d = i & j;
			if(d < c)
				cont++;
			//printf("%d\n", cont);
		}
	}

	return cont;
}

int main(){
	int t, a, b, c, cases;

	scanf("%d", &t);

	for(cases = 1; cases <= t; cases++){
		scanf("%d %d %d", &a, &b, &c);

		printf("Case #%d: %d\n", cases, calcular(a, b, c));
	}
}
