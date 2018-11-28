#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <map>
#include <vector>
#include <string>
#include <cctype>
#include <set>
#include <utility>
#include <stack>
#include <iostream>

using namespace std;

int t,k,n;
typedef long long ll;

int keys[45];
int ki[30][45];
int kn[30];
int tipo[30];

int nec[205];
int tot[205];

struct estado{
	int at;
	int x;
	string lex;
	estado(){}
	estado(int att, int xx, string l){
		at = att;
		x = xx;
		lex = l;
	}
	const bool operator< (const estado &that) const{
		//if(x != that.x) return x > that.x;
		//return at > that.at;
		return lex > that.lex;
	}
};

bool mark[1<<21];
int pai[1<<21];
char aux [30][5];

int main (){
	#ifdef INTERNO
		freopen("in", "r", stdin);
		freopen("out", "w", stdout);
	#endif
	for(int i = 0; i < 28; ++i) sprintf(aux[i], "%02d ", i);
	scanf("%d", &t);
	for(int _ = 1; _ <= t; ++_){
		//memset(nec, 0, sizeof nec);
		//memset(tot, 0, sizeof tot);
		memset(mark, 0, sizeof mark);
		scanf("%d %d\n", &k, &n);
		for(int i = 0; i < k; ++i){
			scanf("%d", keys+i);
			//tot[keys[i]]++;
		}
		for(int i = 0; i < n; ++i){
			int ti, kk;
			scanf("%d %d", &ti, &kk);
			tipo[i] = ti;
			//nec[ti]++;
			kn[i] = kk;
			for(int j = 0; j < kk; ++j){
				 scanf("%d", &ki[i][j]);
				 //tot[ki[i][j]]++;
			}
		}
		priority_queue<estado> fila;
		fila.push(estado(0,0,""));
		estado atual;
		int tem[50];
		int quer[50];
		int fimm = 1<<n;
		//for(int i = 1; i < 201; ++i) if(nec[i] > tot[i]) goto fim;
		mark[0] = true;
		while(fila.size()){
			atual = fila.top(); fila.pop();
		//for(int zzz = 0; zzz < fimm; ++zzz){
			//if(!mark[zzz]) continue;
			int tt = k;
			int qq = 0;
			int at = atual.at;
			memcpy(tem, keys, (k<<2));
			for(int i = 0; i < n; ++i) if(at&(1<<i)){
				//if(kn[i]){
				//	memcpy(tem+tt, ki[i], kn[i]<<2);
				//	tt += kn[i];
				//}
				for(int j = 0; j < kn[i]; ++j) tem[tt++] = ki[i][j];
				quer[qq++] = tipo[i];
			}
			sort(tem,tem+tt);
			sort(quer,quer+qq);
			int novot = 0;
			int novoq = 0;
			for(int i = 0; i < tt; ++i){
				if(novoq < qq && tem[i] == quer[novoq]) ++novoq;
				else tem[novot++] = tem[i];
			}
			tt = novot;
			tem[tt++] = 999;
			for(int i = 0; i < n; ++i) if(!(at&(1<<i))){
				int novoat = at|(1<<i);
				if(mark[novoat]) continue;
				int low = *lower_bound(tem,tem+tt,tipo[i]);
				if(low == tipo[i]){
					mark[novoat] = true;
					pai[novoat] = i;
					fila.push(estado(novoat,atual.x+1,atual.lex+aux[i]));
				}
			}
		}
		
		fim:
		if(mark[(1<<n)-1]){
			 printf("Case #%d:", _);
			 int estou = (1<<n)-1;
			 int total = 0;
			 do{
			 	tem[total++] = pai[estou];
			 	estou ^= (1<<pai[estou]);
			 }while(estou);
			 reverse(tem, tem+total);
			 for(int i = 0; i < total; ++i)
				printf(" %d", tem[i]+1);
			 printf("\n");
		}
		else printf("Case #%d: IMPOSSIBLE\n", _);
	}
	return 0;
}
