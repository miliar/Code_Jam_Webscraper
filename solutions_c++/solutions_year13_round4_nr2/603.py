#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<iostream>
#include<cmath>
using namespace std;
long long t,p,n,m;
long long can(){
	long long nn=n;
	long long ans=1;
	while(m<nn){
		nn/=2;
		ans*=2;
	}
	return n-ans+1; 
}
long long must(){
	if(n==m)return n;
	long long nn=n,now=0;
	int ans=1;
	while(m>now){
		nn/=2;
		now=now+nn;
		ans*=2;
	}
	return ans-1; 
}
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%lld",&t);
	for(int q=1;q<=t;q++){
		scanf("%lld%lld",&p,&m);
		n=1;
		for(int i=1;i<=p;i++)
			n*=2;
		printf("Case #%d: %lld %lld\n",q,must()-1,can()-1);
	}
	return 0;
}
