#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;

#define nMax 1100

#define bug puts("Fuck");

bool is[nMax];
int a[nMax];

bool check(int n){
	if(n>=nMax) return false;
	int l=0;
	while(n){
		a[l++]=n%10;
		n/=10;
	}
	for(int i=0;i<l;i++)if(a[i]!=a[l-i-1]) return false;
	return true;
}

void init(){
	memset(is,0,sizeof(is));
	is[1]=1;
	for(int i=2;i<nMax;i++){
		if(check(i) && check(i*i))is[i*i]=1;
	}
}


int main(){
	init();
    freopen("C-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int cas = 1;
    while(t--){
		int a,b,ans=0;
		scanf("%d%d",&a,&b);
		for(int i=a;i<=b;i++) ans+=is[i];
		printf("Case #%d: %d\n",cas++,ans);
	}
	return 0;
}
