#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <cstring>
#include <stack>

using namespace std;
typedef vector<int> VI;

typedef unsigned long long ull;

void binario(int x, VI &s){
	while(x){
		s.push_back(x%2);
		x/=2;
	}
}

void print(VI s){
	for(int i=s.size()-1; i>=0; i--) printf("%d", s[i]);
}

ull divisor(ull x){
	for(ull i=2; i<x; ++i) if(x%i==0) return i;
}

bool ehprimo(ull x){
	for(ull i=2; i*i<=x; ++i) if(x%i==0) return false;
	return true;
}

int main(){
	char str[40];
	ull bases[11];
	ull pot[11][33];
	int i, j;
	for(i=1; i<=10; ++i){
		pot[i][0]=1;
	}
	for(i=1; i<=10; ++i){
		for(j=1; j<=32; j++){
			pot[i][j]=pot[i][j-1]*i;
		}
	}
	
	/*for(i=0; i<3; ++i){
		for(j=0; j<=32; ++j){
			printf("%d^%d=%llu\n", i, j, pot[i][j]);
		}
	}*/
	
	/*scanf("%s", str);
	
	int t = strlen(str);
	
	for(i=2; i<=10; ++i){
		bases[i]=0;
		for(j=0; j<t; ++j){
			bases[i]+=(str[t-1-j]-'0')*pot[i][j];
		}
		printf("%d\n", bases[i]);
	}*/
	
	int testes, tam, exe;
	scanf("%d", &testes);
	for(int ct=1; ct<=testes; ++ct){
		printf("Case #%d:\n", ct);
		scanf("%d %d", &tam, &exe);
		int cont=0;
		for(int cand=(1<<(tam-1))+1; cont<exe; cand+=2){
			VI vet;
			binario(cand, vet);
			//printf("#"); print(vet); printf("\n");
			int b;
			for(b=2; b<=10; ++b){
				bases[b]=0;
				for(j=0; j<vet.size(); ++j){
					bases[b]+=vet[j]*pot[b][j];
				}
				//printf("base %d %d\n", b, bases[b]);
				if(ehprimo(bases[b])) break;
			}
			if(b>10){
				print(vet);
				for(int i=2; i<=10; ++i) printf(" %llu", divisor(bases[i]));
				printf("\n");
				cont++;
			}
		}
	}	
}
