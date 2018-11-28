#include <stdio.h>

int numeri[10];
int test;
unsigned long long c=1;
unsigned long long numero;
unsigned long long insert;

int controlla(){
	int c=1;
	for(int e=0;e<10;e++){
		if(numeri[e]==0){
			c=0;
			}
		}
	return c;
	}
	void clear(){
		for(int i=0;i<10;i++){
			numeri[i]=0;
			}
		}

void scomponi(unsigned long long n ){
	if(n<10){
		numeri[n]++;
		
	}else{
		unsigned long long a;
		a=n/10;
		int mod=n % 10;
		numeri[mod]++;
		scomponi(a);
		}
	}
	
void conta(unsigned long long num, int f){
	if(num==0){
		printf("Case #%d: INSOMNIA\n",f+1);
		return;
		}else{
			int b= controlla();
	if(b==0){
		unsigned long long b = num*c;
		scomponi(b);
		c++;
		numero=b;
		conta(num,f);
		}else{
			 printf("Case #%d: %llu\n",f+1,numero);
			 numero=0;
			 clear();
			 c=1;
			}
	
}
	
	}
	
		int main(){
	scanf("%d",&test);
	for(int i=0;i<test;i++){
		scanf("%llu",&insert);
		conta(insert,i);
		
		
		}
	
	
	return 0;
	
	}
		
