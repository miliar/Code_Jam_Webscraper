#include <iostream>
#include <cstdio>


using namespace std;

int main()
{
	
	int T,i,n=0;
	double C,F,X,t,t1,t2,cur;
	scanf("%d",&T);
	while(T--)
	{
		n++;
		cur=2.0;
		t=0;
		scanf("%lf %lf %lf",&C,&F,&X);
		while((X/cur)>(C/cur+X/(cur+F)))
		{
			t+=C/cur;
			cur=cur+F;
		}
		t+=(X/cur);
		printf("Case #%d: %lf\n",n,t);
	}
	
	
	return 0;
}
