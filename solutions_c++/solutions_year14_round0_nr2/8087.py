#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
	int test,t;
	double ts,x,c,f,best_sol,r;
	cin>>test;
	for(t=1;t<=test;t++)
	{
		cin>>c>>f>>x;
		r=2;
		
		best_sol=x/r;
		ts=c/r;
		r+=f;
		//while(comp(ts,best_sol)<0){
		while(ts<best_sol)
		{
		 	best_sol=min(best_sol,ts+x/r);
			ts+=c/r;
			r+=f;
		}
		printf("Case #%d: %.7lf\n",t,best_sol);
	}
	return 0;
}

