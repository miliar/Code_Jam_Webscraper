#include <vector>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <cstdio>
using namespace std;
#define FOR(i,j,k) for(i=j;i<=k;i++)
double C,F,X;

double work()
{
	double ans,now,res=0;
	ans=X/2;
	now=2;
	while(1)
	{
		res+=C/now;
		now+=F;
		if(res+X/now>=ans)break;
		ans=res+X/now;
	}
	return ans;
}

int main()
{
	int i,T;
	scanf("%d",&T);
	FOR(i,1,T)
	{
		cin>>C>>F>>X;
		printf("Case #%d: %.7f\n", i,work());
	}
}