#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <cstring>

using namespace std;
typedef vector<int> VI;

char s[105];
int tam, ult;

void troca(char &c){ c=(c=='+'?'-':'+'); }

void flipinv(int p){ /* 0 eh todos */
	for(int i=0; i<p-i; i++){
		swap(s[i], s[p-i]);
	}
	for(int i=0; i<=p; ++i) troca(s[i]);
}

bool acabou(){
	for(int i=0; i<tam; ++i) if(s[i]=='-') return false;
	return true;
}

int main(){
	int N;
	scanf("%d\n", &N);
	for(int t=0; t<N; ++t){
		int troca=0;
		scanf("%s\n", s);
		tam = strlen(s);
		ult = tam-1;
		while(!acabou()){
			int ini = ult;
			while(s[ini]=='+') ini--;
			/*garantir que o primeiro seja -*/
			if(s[0]=='+'){
				int p=0;
				while(s[p]=='+') p++;
				p--;
				flipinv(p);
				troca++;
			}
			troca++;
			flipinv(ini);
		}
		//puts(s);
		//puts("____");
		printf("Case #%d: %d\n", t+1, troca);
	}
}
