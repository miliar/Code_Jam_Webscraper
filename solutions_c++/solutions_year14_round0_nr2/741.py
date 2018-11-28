/*Vladimir Ignatiev 2014*/
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>

using namespace std;

#define rep(A,B) for(int A=0;A<B;++A)
#define repi(A,I,B) for(int A=I;A<B;++A)
#define repd(A,B) for(int A=B-1;A>=0;--A)
#define repdi(A,I,B) for(int A=B-1;A>=I;--A)
#define repall(A,F) for_each(A.begin(),A.end(),F);

double C, F, X;

double f()
{	
	double prod=2;
	double time=0;

	while(1)
	{
		double res1=time+C/prod+X/(prod+F);
		double res2=time+X/prod;
	
		if(res2<res1) return res2;

		time+=C/prod;
		prod+=F;
	}

	return 0;
}

int main()
{
	FILE* In=fopen("B.in","r");if(!In) return 1;
	FILE* Out=fopen("B.res","w");if(!Out) return 2;

	int nCount;
	fscanf(In,"%d",&nCount);
	rep(i,nCount)
	{
		fprintf(Out,"Case #%d: ",i+1);
		printf("%d\n",i);
		fscanf(In,"%lf%lf%lf",&C,&F,&X);

		double res=f();
		fprintf(Out,"%.7f\n",res);
	};
	fclose(In);
	fclose(Out);
	return 0;
}