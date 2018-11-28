#include <bits/stdc++.h>

using namespace std;

int main(){
	unsigned long long int x,aux;
	int t,c;
	c = 0;
	scanf("%d",&t);
	while(t--){
		printf("Case #%d: ",++c);
		scanf("%llu",&x);
		int v[10] = {0};
		int cont = 0;
		int imp = 0;
		int i  = 0;
		int rest;
		int rr;
		while(cont < 10 && !imp){
			i++;
			aux = i*x;
			if(aux == x && i > 1){
				imp = 1;
			}
			else{
				while(aux){
					rest = aux%10;
					if(!v[rest]){
						cont++;
					}
					v[rest] = 1;
					aux/=10;
				}
			}
		}
		if(imp){
			printf("INSOMNIA\n");
		}
		else{
			printf("%llu\n",i*x);
		}
	}
	return 0;
}