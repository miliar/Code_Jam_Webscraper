#include <stdio.h>
#include <string.h>

int T, u, N, M, resp, temp;
int tabela[110][110];
char c;

bool g(int a, int b, int d){
	int vx, vy;
	if(d==1) {
		vx = 1;
		vy = 0;
	}
	if(d==2) {
		vx = 0;
		vy = 1;
	}
	if(d==3) {
		vx = 0;
		vy = -1;
	}
	if(d==4) {
		vx = -1;
		vy = 0;
	}
	
	for(int k=1;;k++){
		if(tabela[a+k*vx][b+k*vy]>0) return true;
		if(tabela[a+k*vx][b+k*vy]<0) return false;
	}
}

int f(int a, int b){
	if(g(a,b,tabela[a][b])) return 0;
	for(int i=1; i<=4; i++){
		if(g(a,b,i)) return 1;
	}
	return -1;
}

int main(){
	scanf(" %d", &T);
	u = 0;
	while(u<T){
		u++;
		scanf(" %d %d", &N, &M);
		resp = 0;
		memset(tabela, -1, sizeof(tabela));
		for(int i=1; i<=N; i++){
			for(int j=1; j<=M; j++){
				scanf(" %c", &c);
				if(c=='.') tabela[i][j] = 0;
				else if(c=='v') tabela[i][j] = 1;
				else if(c=='>') tabela[i][j] = 2;
				else if(c=='<') tabela[i][j] = 3;
				else tabela[i][j] = 4;
			}
		}
		
		for(int i=1; i<=N && resp>=0; i++){
			for(int j=1; j<=M && resp>=0; j++){
				if(tabela[i][j]>0){
					temp = f(i,j);
					if(temp == -1) resp = -1;
					else resp += temp;
				}
			}
		}
		
		if(resp<0) printf("Case #%d: IMPOSSIBLE\n", u);
		else printf("Case #%d: %d\n", u, resp);
	}
	return 0;
}
