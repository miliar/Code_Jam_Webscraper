#include<stdio.h>
#include<math.h>

int pali(int x){
	int aux = x;
	int num[5];
	int p=0;
	while(aux){
		num[p]=aux%10;
		aux = aux/10;
		p++;
	}
	for(int i=0;i<p;i++){
		aux += num[i]*pow(10,(p-i)-1);
	}
	if(aux==x)return 1;
	return 0;
}

int main(){
	
	int a, b;
	int i, k, t;
	int fs[100];
	fs[0]=0;
	fs[1]=1;
	for(i=2;i<=33;i++){
		fs[i]=fs[i-1];
		if(pali(i)){
			if(pali(i*i))fs[i]++;
		}
	}
	

	
	scanf("%d", &t);
	for(k=1;k<=t;k++){
		scanf("%d %d", &a, &b);
		int aa=sqrt(a);
		int bb=sqrt(b);
		if(((aa*aa)==a)&&pali(a)){
			if(pali(aa))aa--;
		}
		printf("Case #%d: %d\n", k, fs[bb]-fs[aa]);
	}	
	
	return 0;
}