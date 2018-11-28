#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;
int main(){
	//freopen("B-large.in","r",stdin);
	//freopen("B-large.out","w",stdout);
	int i,j,m,n,T,vcase=0;
	double c,f,x,v,t;
	scanf("%d",&T);
	while(T--){
		v=2;t=0;
		scanf("%lf%lf%lf",&c,&f,&x);
		while(1){
			if(x/v<c/v+x/(v+f)){
				t+=x/v;
				break;
			}
			else{
				t+=c/v;
				v+=f;
			}
		}
		printf("Case #%d: %.7lf\n",++vcase,t);
	}
	return 0;
}