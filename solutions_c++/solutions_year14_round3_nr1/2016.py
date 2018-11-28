#include <cstdio>
#include <algorithm>
using namespace std;

int t,p,q, pot[50];

int nwd(int a, int b){
	int pom;
	while(b!=0){
		pom=b;
		b=a%b;
		a=pom;
	}
	return a;
}

bool czypot(int x){
	int l=0;
	while(pot[l]<x && l<41) l++;
	if(pot[l]==x) return true;
	return false;
}

int main(){
	pot[0]=1;
	for(t=1;t<=40;t++) pot[t]=pot[t-1]<<1;
	scanf("%d", &t);
	for(int k=0;k<t;k++){
		char c;
		scanf("%d%c%d", &p, &c, &q);
		printf("Case #%d: ", k+1);
		int nw=nwd(p,q); p/=nw; q/=nw;
		if(!czypot(q)) printf("impossible\n");
		else{
			int ans=0;
			while(q>p){ 
				q>>=1;
				ans++;
			}
			printf("%d\n", ans);
		}
	}
	return 0;
}
