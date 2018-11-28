#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<queue>
#include<stack>
#include<cmath>
using namespace std;
typedef pair<int,int> PI;
typedef long long LL;
typedef double D;
#define FI first
#define SE second
#define MP make_pair
#define PB push_back
#define R(I,N) for(int I=0;I<N;I++)
#define F(I,A,B) for(int I=A;I<B;I++)
#define FD(I,N) for(int I=N-1;I>=0;I--)
#define make(A) scanf("%d",&A);
int n;
LL p;
LL licz2(){
	LL pom=1;
	int nn=0;
	while(pom*2<=p){
		nn++;
		pom*=2;
	}
	return (1ll<<(n-nn));
}
void licz(){
	scanf("%d%lld",&n,&p);
	if(p==(1ll<<n)){
		printf("%lld %lld\n",(1ll<<n)-1,(1ll<<n)-1);
		return;
	}
	p = (1ll<<n) - p;
	printf("%lld ",licz2()-2);
	p = (1ll<<n) - p;
	printf("%lld\n",(1ll<<n)-licz2());
}
main(){
	int _;
	make(_);
	R(t,_){
		printf("Case #%d: ",t+1);
		licz();
	}
}