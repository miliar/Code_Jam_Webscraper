#include<iostream>
#include<cstdio>
#include<queue>
#include<vector>
#include<algorithm>
#include<cstring>
using namespace std;

typedef long long ll;

int main(){
	int t,l=0;
	scanf("%d",&t);
	while(l++<t){
		double c,f,x;
		scanf("%lf%lf%lf",&c,&f,&x);
		double a=x/2.0;
		double r=2.0;
		double k=c/r;
		r+=f;
		double b=k+x/r;
		while(b<a){
			a=b;
			k+=c/r;
			r+=f;
			b=k+x/r;
			//if(a<k+
		}
		printf("Case #%d: %.8lf\n",l,a);
	}
	return 0;
}