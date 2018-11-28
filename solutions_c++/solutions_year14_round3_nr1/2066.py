#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
int gcd(int a, int b){
	if(b==0)return a;
	return gcd(b, a%b);
}
int check(int q){
	for(int i = 1; i<=40;i++){
		long long temp = (long long)1 << i;
		if(temp%q==0)return(i);
	}
	return 0;
}
int main(){
	int t,p,q;
	freopen("1.in","r",stdin);
	scanf("%d\n",&t);
	for(int i=1;i<=t;i++){
		scanf("%d/%d\n",&p,&q);
		printf("Case #%d: ",i);
		int found = 0;
		for(int i = 1; i<=40; i++){
			int d = gcd(p,q);
			p/=d;
			q/=d;
			if(p>q)break;
			if(!((q & (q-1)) == 0))break;
			if(p+p-q>=0&&p+p-q<=q){
				printf("%d\n",i);
				found = 1;
				break;
			}
			p+=p;
		}
		if(!found)printf("impossible\n");
	}
	fclose(stdin);
	return(0);
}
