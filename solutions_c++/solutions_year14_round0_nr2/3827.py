#include<iostream>
#include<cstdio>
using namespace std;
int t;
double c,f,x;
int main(){
	freopen("2.in","r",stdin);
	scanf("%d",&t);
	for(int k=1;k<=t;k++){
		scanf("%lf%lf%lf",&c,&f,&x);
		double v = 2;
		double ans = x / v;
		double past = 0;
		for(int i = 1; 1; i++){
			past+=c/v;
			v+=f;
			double rest = x / v;
			if(past+rest<ans)ans=past+rest;
			else break;
		}
		printf("Case #%d: %.7lf\n",k,ans);
	}
	fclose(stdin);
	return 0;
}
