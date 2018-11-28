#include <stdio.h>
#include <math.h>

unsigned long long qpal[10000100];
unsigned long long at;

bool isPalindrome(unsigned long long x){
	if(x%10==0)return false;
	unsigned long long y=0,z=x;
	while(z!=0){
		y*=10;
		y+=z%10;
		z/=10;
	}
	if(x==y)return true;
	return false;
}

int main(){
	at=0;
	for(unsigned long long i=0;i<10000001;i++){
		if(i!=0)qpal[i]=qpal[i-1];
		if(isPalindrome(i)){
			if(isPalindrome(i*i)){
				qpal[i]++;

				//printf("%llu %llu\n",i*i,qpal[i]);
			}
		}
	}
	unsigned long long t,a,b,p,q;

	scanf("%llu",&t);
	for(int xxx=0;xxx<t;xxx++){
		scanf("%llu %llu",&a,&b);
		p=sqrt(a);
		q=sqrt(b);
		//printf("%llu",p);
		p=(p*p==a)?p:p+1;
		printf("Case #%d: %llu\n",xxx+1,qpal[q]-qpal[p]+((qpal[p-1]==qpal[p])?0ULL:1ULL));
		

	}
}