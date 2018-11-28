#include<cstdio>
#include<iostream>
using namespace std;
int main() {
	int t;
	scanf("%d",&t);
	for(int l=1;l<=t;l++){
		long double c,f,x,p=0.0,m,bp=0.0,z=2.0,q=0.0;
		scanf("%Lf%Lf%Lf",&c,&f,&x);
		p=x/z;
		bp=c/z;
		z=z+f;
		m=x/z;
		while(p>bp+m){
			q=bp;
			p=q+x/z;
			bp=q+c/z;
			z=z+f;
			m=x/z;
		}
		printf("Case #%d: %0.6Lf\n",l,p);
	}
	return 0;
}
