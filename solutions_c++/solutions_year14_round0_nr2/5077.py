#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<string.h>
#include<map>
#include<cmath>
#include<iomanip>
#include<vector>
#include<queue>
using namespace std;
typedef long long LL;



int main(){
	int t;
	scanf("%d",&t);
	int z=t;
	while(t--)
	{
		double c,f,x;
		scanf("%lf %lf %lf",&c,&f,&x);
		double r=2,time=0;
		double s=(c/r)+(x/(r+f));
		while((x/r)>s)
		{
			time+=c/r;
			r+=f;
			s=(c/r)+(x/(r+f));
		}
		time+=(x/r);
		printf("Case #%d: %.7lf\n",z-t,time);
	}
	   
    return 0;
}
