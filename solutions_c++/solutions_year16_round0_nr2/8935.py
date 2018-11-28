#include <cstdio>
#include <cstring>

using namespace std;

char stack[200];

void revstack(int n, int m){
	char aux;
	int i=m, j=n;
	while(j<i){
		aux = stack[i]=='+'?'-':'+';
		stack[i] = stack[j]=='+'?'-':'+';
		stack[j] = aux;
		i--;
		j++;
	}
	if(j==i)
		stack[i] = stack[i]=='+'?'-':'+';
	return;
}

int calc(int tam){
	int it=tam;
	char fst;
	bool fim = 1;
	int ans = 0;
	while(it>=0){
		fim = 1;
		it = tam;
		fst = stack[0];
		while((stack[it]!='-') && (it)){
			it--;
		}
		if(fst=='+'){
			while((stack[it]!='+') && (it)){
				fim = 0;
				it--;
			}
		}
		if(!it && fim)
			break;
		//printf("it(%d) = %s\n", it, stack);
		revstack(0, it);
		//printf("virou -> %s\n", stack);
		ans++;
		//gira e soma 1
	}
	if(stack[0] == '-')
		ans++;
	return ans;
}

int main() {
	int n;
	scanf("%d\n", &n);
	for(int i=0; i<n; i++){
		scanf("%s", stack);
		printf("Case #%d: %d\n", i+1, calc((int)strlen(stack)));
	//	revstack(0, 6);
	//	printf("%s", stack);
	}
	return 0;
}
