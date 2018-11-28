#include <bits/stdc++.h>

int t,n,caso=0,vet[20],resp,dig,cont=0,k=1,aux;

int main(){
	scanf("%d",&t);
	while(t--){
		scanf("%d",&n);
		if(n==0)
			printf("Case #%d: INSOMNIA\n",++caso);
		else{
			for(int i = 0 ; i <= 9 ; i++)
				vet[i]=0;
			while(cont!=10){
				aux=n*k;
				resp=aux;
				while(aux){
					dig=aux%10;
					aux/=10;
					if(vet[dig]==0){
						vet[dig]=1;
						cont++;
					}
				}
				k++;
			}
			cont=0;
			k=1;
			printf("Case #%d: %d\n",++caso,resp);
		}
	}
}
