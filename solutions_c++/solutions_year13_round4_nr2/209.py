#include<stdio.h>
#include<algorithm>

typedef long long int lnt;
typedef double dou;
using namespace std;
lnt fb(lnt n,lnt p){
	lnt nn=(1ll<<n);
	if(p==nn)
		return nn-1;
	if(p==nn-1)
		return nn-2;
	if(p<=nn/2)
		return 0;
	return fb(n-1,p-nn/2)*2+2;
	}
lnt fa(lnt n,lnt p){
	lnt nn=(1ll<<n);
	if(p==nn)
		return p-1;
	if(p>=nn/2)
		return nn-2;
	return fa(n-1,p)*2;
	}

lnt n,p;
void truli(int uuu){
	scanf("%I64d %I64d",&n,&p);
	lnt ansa=fa(n,p),ansb=fb(n,p);
	printf("Case #%d: %I64d %I64d\n",uuu,ansb,ansa);
	}

int main(){
	freopen("B-large.in","r",stdin);
	freopen("PB-largeout.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int ti=1;ti<=t;ti++)
		truli(ti);
	
	return 0;
	}
