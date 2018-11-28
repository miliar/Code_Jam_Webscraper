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
typedef long double D;
#define FI first
#define SE second
#define MP make_pair
#define PB push_back
#define R(I,N) for(int I=0;I<N;I++)
#define F(I,A,B) for(int I=A;I<B;I++)
#define FD(I,N) for(int I=N-1;I>=0;I--)
#define make(A) scanf("%d",&A);
#define MAX 37
LL b;
int n;
LL t[MAX];
LL licz(LL lim){
	LL wyn=0;
	R(i,n)wyn+=max(lim-t[i],0ll);
	return wyn;
}
D w(LL war){
	int il=0;
	R(i,n)if(t[i]<=war)il++;
	int zos = b-licz(war);
	D wyn = 0.;
	while(il>0 && zos>=0){
		LL s = 0;
		for(int i=0;i<il;i++){
			s += war-t[i];
		}
		D pom = 36*D(s)/il + zos;
		if(pom>wyn)wyn=pom;
		zos--;
		il--;
	}
	return wyn;
}
void test(){
	scanf("%lld%d",&b,&n);
	R(i,n)scanf("%lld",&t[i]);
	F(i,n,37)t[i]=0;
	n=37;
	sort(t,t+n);
	F(i,1,n)t[i]-=t[0];
	t[0]=0;
	LL p=0,k=b+1;
	while(p+1!=k){
		LL m=(p+k)/2;
		if(licz(m)<=b)
			p=m;
		else
			k=m;
	}
	D wyn = b;
	for(int i=0; i<=37;i++){
		if(p <= i) break; 
		D pom = w(p-i);
		if(pom>wyn)wyn=pom;
	}
	printf("%.7f\n",double(wyn-b));
}
main(){
	int _;
	make(_);
	R(i,_){
		printf("Case #%d: ",i+1);
		test();
	}
}