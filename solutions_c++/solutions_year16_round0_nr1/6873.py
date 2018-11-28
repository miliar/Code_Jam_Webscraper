#include <cstdio>

using namespace std;

int tab[10], n, t;

void rozloz(int x){
	while (x != 0){
		tab[x % 10] = 1;
		x /= 10;
	}
}

bool ok(){
	int suma = 0;
	for (int i = 0; i <= 9; i++)
		suma += tab[i];
	return suma == 10;
}
// 72 powtorzenia
void clear(){
	for (int i = 0; i <= 9; i++)
		tab[i] = 0;
}

int main()
{
	scanf("%d",&n);
	for (int i = 1; i <= n; i++){
		scanf("%d",&t);
		if (t == 0) printf("CASE #%d: INSOMNIA\n", i);
		else{
			int pom = 0;
			for (int j = 1; j <= 72; j++){
				rozloz(t * j);
				if (ok()) {pom = j; break;}
			}
			if (pom != 0) printf("CASE #%d: %d\n", i, t * pom);
			clear();
		}
	}
	return 0;
}
