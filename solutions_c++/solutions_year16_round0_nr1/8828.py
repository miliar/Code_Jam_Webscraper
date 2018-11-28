#include <cstdio>
#include <cstring>

using namespace std;

int foi[int(2<<10)+1];

void calc(int m){
	int vez = 0, aux = m, digs = 0, atual;
	do {
		digs|= (1<<(aux%10));
		aux/=10;
	} while(aux>0);
	foi[digs] = 1;
	atual = m;
	while(digs!=1023){
		atual += m;
		aux = atual;
		vez = 0;
		//printf("%d ->", atual);
		do {
			digs|= (1<<(aux%10));
			vez|= (1<<(aux%10));
			aux/=10;
		} while(aux>0);
		if(foi[vez]==20) //mudar constante
			break;
		foi[vez]++;
	}
	if(digs==1023)
		printf("%d\n", atual);
	else
		printf("INSOMNIA\n");
}

int main() {
	int n, m;
	scanf("%d", &n);
	for(int i=0; i<n; i++){
		scanf("%d", &m);
		memset(foi, 0, sizeof(foi));
		printf("Case #%d: ", i+1);
		calc(m);
	}
	return 0;
}
