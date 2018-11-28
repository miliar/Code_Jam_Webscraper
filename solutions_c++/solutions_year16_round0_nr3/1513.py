#include<cstdio>
#include<algorithm>

using namespace std;
typedef long long int lint;
const int MAX_P = 1000;

int np, csf, vis[MAX_P];
lint primo[MAX_P], prova[16];

void crivo(){
	np = 0;
	for(int i=2;i<MAX_P;i++) vis[i] = 0;
	for(int i=2;i<MAX_P;i++){
		if(!vis[i]){
			primo[np++] = (lint)i;
			for(int j=i;j<MAX_P;j+=i) vis[j] = 1;
		}
	}
}

int provaide(lint coin, lint p, int b){
	lint curr = 0LL, x = 1LL;
	for(int i=0;i<=31;i++){
		if(coin&(1LL<<i)) curr += x;
		curr %= p;
		x = (x*(lint)b)%p;
	}
	return curr == 0 ? 1 : 0;
}

int main(){
	int casos, len, csf_tot;
	scanf(" %d %d %d", &casos, &len, &csf_tot); len--;
	csf = 0;
	crivo();
	printf("Case #1:\n");
	for(lint coin=(1LL<<len)+1;csf<csf_tot;coin+=2LL){
		int base;
		for(base=2;base<=10;base++){
			prova[base] = 0;
			for(int i=0;i<np && !prova[base];i++) if(provaide(coin, primo[i], base)) prova[base] = primo[i];
			if(!prova[base]) break;
		}
		if(base == 11){
			for(int i=len;i>=0;i--) printf("%d", coin&(1LL<<i) ? 1 : 0);
			for(int i=2;i<=10;i++) printf(" %lld", prova[i]); printf("\n");
			csf++;
		}
	}
	return 0;
}
