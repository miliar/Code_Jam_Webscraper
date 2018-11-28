#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
using namespace std;
int n,m,T,co,a[40],prime[]={2,3,5,7,11,13,17,19,23,29};
bool isprime(int base, int mod){
	int res=0;
	for(int i=n-1;i>=0;--i)
		res=(res*base+a[i])%mod;
	return res != 0;
}
bool check(){
	for(int i=2;i<=10;++i){
		int yes=true;
		for(int j=0;j<10;++j)
			if(!isprime(i, prime[j]))
				yes=false;
		if(yes)return 0;
	}
	return 1;
}
void dfs(int now){
	if(co==m)return;
	if(now==1){
		if(check()) {
			for(int i=n-1;i>=0;--i)
				printf("%d",a[i]);
			for(int i=2;i<=10;++i)
				for(int j=0;j<10;++j)
					if(!isprime(i, prime[j])) {
						printf(" %d", prime[j]);
						break;
					}
			printf("\n");
			++co;
		}
		return;
	}
	a[now]=0;
	dfs(now-1);
	a[now]=1;
	dfs(now-1);
}
int main() {
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int i=1; i<=T; ++i){
		scanf("%d%d",&n,&m);
		co=0;
		for(int j=0;j<n;j++)a[j]=0;
		a[0]=a[n-1]=1;
		printf("Case #%d:\n",i);
		dfs(n-2);
	}
	return 0;
}
