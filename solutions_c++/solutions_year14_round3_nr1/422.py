#include <iostream>
#include <math.h>
#include <algorithm>
#include <string>
#include <cstdio>

#define SC(x) scanf("%d", &x);
#define File freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);

using namespace std;
const long long inf =2147483647;
const int md=1e9+7;
const double eps=1e-6;

int n,m,i,j,k,ttt,tt;
long long ans,p,q;

int main(){
	File;
	SC(ttt);
	for (tt=1; tt<=ttt; tt++){
		printf("Case #%d:",tt);
		scanf("%lld/%lld",&p,&q);
		int g=__gcd(p,q);
		p/=g;
		q/=g;
		long long d2=1;
		int d=0;
		while (d2<q){
			d++;
			d2<<=1;
		}
		if (d2>q || d>40 || p>q || p<=0){
			printf(" impossible\n");
			continue;
		}
		/*long long pd=0, pd2=1;
		while (pd2<p){
			pd++;
			pd2<<=1;
		}
		if (pd2>p) pd--;
		printf(" %d",int(d-pd));*/
		while (p>1){
			d--;
			p>>=1;
		}
		printf(" %d",d);
		printf("\n");
	}
	return 0;
}
