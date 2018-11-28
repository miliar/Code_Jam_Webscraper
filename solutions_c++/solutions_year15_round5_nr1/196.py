#include <stdio.h>
#include <string.h>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

struct inter{
	int ini, fim, pos;
};

bool compara1(inter a, inter b){
	return a.ini < b.ini;
}

bool compara2(inter a, inter b){
	return a.fim < b.fim;
}


int T,u,N,D,as,cs,rs,am,cm,rm, resp;
int s[1000100];
int m[1000100];
vector<int> v[1000100];
inter x[1000100];
inter z[1000100];

map<int, vector<int>> inis;

void f(int pos, int min, int max) {
	if(s[pos] < min) min = s[pos];
	if(s[pos] > max) max = s[pos];
	
	if(max - min > D) {
		x[pos].ini = 2*D;
		x[pos].fim = 2*D;
		x[pos].pos = pos;
	
		z[pos].ini = 2*D;
		z[pos].fim = 2*D;
		z[pos].pos = pos;
	}
	else {
		x[pos].ini = min;
		x[pos].fim = max;
		x[pos].pos = pos;
	
		z[pos].ini = min;
		z[pos].fim = max;
		z[pos].pos = pos;
	}
	
	for(int i=0; i<v[pos].size(); i++){
		f(v[pos][i],min,max);
	}
}

int main(){
	scanf(" %d", &T);
	u=0;
	while(u<T){
		u++;
		scanf(" %d %d", &N, &D);
		scanf(" %d %d %d %d", &s[0], &as, &cs, &rs);
		scanf(" %d %d %d %d", &m[0], &am, &cm, &rm);

		v[0].clear();
		for(int i=1; i<N; i++){
			v[i].clear();
			s[i] = (s[i-1]*as+cs)%rs;
			m[i] = (m[i-1]*am+cm)%rm;
			v[m[i]%i].push_back(i);
		}
		for(int i=N-1; i>=0; i--) {
			s[i] -= s[0];
		}
		
		f(0, 0, 0);
		
		resp = 0;
		
		sort(x, x+N, compara2);
		sort(z, z+N, compara1);
		int atual = 0;
		int novo_fim, novo_ini;
		int pos_fim = 0;
		int pos_ini = 0;
		while(pos_fim < N){
			novo_fim = x[pos_fim].fim;
			while(x[pos_fim].fim == novo_fim && pos_fim < N){
				pos_fim++;
				atual++;
			}
			novo_ini = novo_fim-D;
			while(z[pos_ini].ini < novo_ini) {
				pos_ini++;
				atual--;
			}
			
			if(atual > resp && novo_ini <= 0 && novo_fim >=0) resp = atual;
		}
		
		printf("Case #%d: %d\n", u, resp);
	}
	return 0;
}
