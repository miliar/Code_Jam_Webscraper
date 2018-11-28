#include <iostream>
#include <math.h>
#include <algorithm>
#include <string>
#include <cstdio>

#define SC(x) scanf("%d", &x);
#define File freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);

using namespace std;
const long long inf =2147483647;
const int md=1e9+7;
const double eps=1e-6;

int n,m,i,j,k,ttt,tt;
long double ans,c,x,f,t,cps,tm;

int main(){
	File;
	SC(ttt);
	for (tt=1; tt<=ttt; tt++){
		scanf("%Lf%Lf%Lf",&c,&f,&x);
		cps=2;
		ans=inf;
		tm=0;
		int kkk=6000500;
		while (kkk--){
			t=x/cps;
			if (t+tm<0) break;
			ans=min(ans,t+tm);
			tm+=c/cps;
			cps+=f;
		}
		printf("Case #%d: %.7Lf\n",tt,ans);
	}
	return 0;
}
