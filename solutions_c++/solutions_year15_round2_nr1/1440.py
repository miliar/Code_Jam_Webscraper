#include <iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
const int N=1000005;
int f[N];
int min(int a,int b){
	return a<b?a:b;
}
int res(int n){
	int res=0;
	while(n){
		res=res*10+n%10;
		n/=10;
	}
	return res;
}
int main(){    
    freopen("t.txt","r",stdin);
	freopen("B_out.txt","w",stdout);
	int n,m,Q,T,Case=1;
	scanf("%d",&T);
	f[1]=1;
	for(int i=2;i<N;i++){
		f[i]=f[i-1]+1;
		if(i%10==0)
			continue;
		m=res(i);
		if(m>=i)
			continue;
		f[i]=min(f[i],f[m]+1);
	}
	while(T--){
		scanf("%d",&n);
		printf("Case #%d: %d\n",Case++,f[n]);
		
	}
    return 0;
}