#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>

#define MAX 110
typedef long long LL;
using namespace std;
LL p,q;
LL  gcd(LL a,LL b){
	LL tmp;
	for(;a%b!=0;){
		tmp=a;
		a=b;
		b=tmp%b;
	}
	return b;
}
int main(){
	int t,i;
	int result;
	char s[200];
	LL gcds;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&t);
	for(i=1;i<=t;++i){
		scanf("%lld/%lld",&p,&q);
		gcds=gcd(q,p);
		q/=gcds;
		p/=gcds;
		if((q&(q-1))!=0){
			cout<<"Case #"<<i<<": impossible"<<endl;
			continue;
		}
		for(result=0;p!=q;){
			if(p%2==0&&q%2==0){
				q/=2;
				p/=2;
			}
			else{
				++result;
				int tmp;
				for(tmp=1;tmp<=p;tmp<<=1);
				tmp/=2;
				p=tmp;
				q/=2;
			}
		}
		if(result>40){
			cout<<"Case #"<<i<<": impossible"<<endl;
			continue;
		}
		cout<<"Case #"<<i<<": ";
		cout<<result<<endl;
	}
	return 0;
}
