#include <bits/stdc++.h>

using namespace std;

int v[5000];

int main(){

	int t,ca = 1;
	scanf("%d",&t);
	while(t--){
		printf("Case #%d: ",ca++);
		int d;
		scanf("%d",&d);

		int resp = 1000000000;
		int maior = 0;
		for(int i = 0;i<d;i++){
			scanf("%d",&v[i]);
			maior = max(maior,v[i]);
		}
		
		for(int i = 1;i<=maior;i++){
			int qtd = 0;
			for(int j = 0;j<d;j++){
				if(v[j]<=i)continue;
				qtd+=((v[j]-i)/i) + ((v[j]-i)%i!=0);
			}
			resp = min(resp,qtd+i);
		}
		printf("%d\n",resp);
	}


	return 0;
}