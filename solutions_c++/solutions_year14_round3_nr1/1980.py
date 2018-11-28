#include <iostream>
#include <cstdio>
using namespace std;

int gcd(int a,int b) {
	if(b==0) return a;
	else return gcd(b,a%b);
}

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int T,P,Q;
	scanf("%d",&T);
	for(int i=1;i<=T;++i) {
		scanf("%d/%d",&P,&Q);
		int tmp=gcd(Q,P);
		P/=tmp , Q/=tmp;
		int mul=1,Pm=-1;
		while(mul<=P) {
			mul<<=1;
			++Pm;
		}
		int Qm=Pm;
		while(mul<Q) {
			mul<<=1;
			++Qm;
		}
		if(mul!=Q) printf("Case #%d: impossible\n",i);
		else printf("Case #%d: %d\n",i,Qm-Pm+1);
	}
	return 0;
}
