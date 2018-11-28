#include<cstdio>

using namespace std;

int main(){
	int j = 1,T;
	scanf("%d",&T);
	while(T--){
		int soma = 0,p = 0,shylv;
		char c;
		scanf("%d",&shylv);
		for(int i=0;i<=shylv;i++){
			scanf(" %c",&c);
			soma += c-48;
			if(i == 0 && soma == 0){
				p += 1;
				soma++;
			}
			if(soma < i+1){
				p += i-soma+1;
				soma++;
			}
		}
		printf("Case #%d: %d\n",j++,p);
	}
	return 0;
}
