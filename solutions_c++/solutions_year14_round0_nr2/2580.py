#include <iostream>
#include <iomanip>
#include <limits>
#include <cstring>

using namespace std;

int t;
double c, f, x, cache[1000001];

void inIt()
{
	memset(cache, 0, sizeof(cache));
	cache[0]=0.0;
	cache[1]=c/2.0;
	for(int i=2 ; i<1000001 ; i++)
		cache[i]=cache[i-1]+c/(f*(1.0*i-1.0)+2.0);
}

int main(void)
{
#ifdef _CONSOLE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);
#endif

	cin>>t;
	for(int j=1 ; j<=t ; j++)
	{
		double sol=numeric_limits<double>::max();
		cin>>c>>f>>x;
		inIt();
		for(int i=0 ; i<100001 ; i++)
			sol=min(sol, cache[i]+x/(f*1.0*i+2.0));

		printf("Case #%d: ", j);
		printf("%.7lf\n", sol);
	}
}