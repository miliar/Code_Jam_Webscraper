#include<cstdio>
#include<cmath>

using namespace std;

int N[20000000];

int CZ(long long a){
	int b=a;
	int c=0;
	while(b){
		c=c*10+(b%10);
		b/=10;
	}
	if(a==c) return 1;
	return 0;
}

void pre(){
	N[0]=1;
	for(long long i=1;i*i<=100000000000000LL;i++){
		if(CZ(i) && CZ(i*i)) N[i]=N[i-1]+1;
		else N[i]=N[i-1];
	}
}

int main(){
	pre();
	
	int t;
	scanf("%d",&t);
	
	for(int i=0;i<t;i++){
		long long a,b;
		scanf("%lld%lld",&b,&a);
		long long A=sqrt(a);
		long long B=sqrt(b);
		if(B*B==b) B--;
		printf("Case #%d: %lld\n",i+1,N[A]-N[B]);
	}
	
   return 0;
}

