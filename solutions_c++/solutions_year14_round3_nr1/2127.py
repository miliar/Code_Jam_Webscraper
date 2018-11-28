#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

long long work(long long p,long long q){
	long long sum=0,tt=-1;
	bool flag=false;
	while (sum<=41&&!flag){
		while (p<q){
			p=p<<1;sum++;
		}
		p-=q;
		if (tt<0) tt=sum;
		if (p==0) flag=true;
	}
	if (!flag) return -1;
	return tt;
}

int main(){
	int cases,n;
	long long p,q;
	freopen("A-small-attempt9.in","r",stdin);
	freopen("AC.out","w",stdout);
	scanf("%d",&cases);
	for (int cas=1;cas<=cases;cas++){
		scanf("%lld/%lld",&p,&q);
		long long ans=work(p,q);
		if (ans>=0) printf("Case #%d: %lld\n",cas,ans);
		else printf("Case #%d: impossible\n",cas);
	}
	return 0;
}
