#include <bits/stdc++.h>
using namespace std;
double solve(double c,double f,double x,double rate)
{
	double sec=0;
	while(1)
	{
		if(x/rate<=(c/rate+x/(rate+f)))
			{
				sec+=x/rate;
				break;
			}
		else 
			{
				sec+=c/rate;
				rate+=f;
			}
	}
	
	return sec;
}
double solve()
{
	int T;
	double c,f,x;
	cin>>T;
	for(int TC=1;TC<=T;TC++)
	{
		cin>>c>>f>>x;
		printf("Case #%d: %.7f\n",TC,solve(c,f,x,2.0));
	}
}
int main()
{
	freopen("gcj2input.txt","r",stdin);
	freopen("gcj2newoutput.txt","w",stdout);
	solve();
	return 0;
}