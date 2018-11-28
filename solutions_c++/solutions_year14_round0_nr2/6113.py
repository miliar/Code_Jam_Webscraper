#include <iostream>
#include <cmath>
#include <cstdio>
using namespace std;

double c, f, x;

void solve ()
{
	scanf("%lf%lf%lf", &c, &f, &x);

	double rate = 2.0;
	double best = x / rate;
	
	double i; double ctime = 0;
	for(i = 1; i < 100000000; i +=1)
	{
                ctime += c/rate;
		rate = rate + f;
		
		if(best >= ctime + x/rate)
			best = ctime + x/rate;
		else
			if(fabs(best - (ctime + x/rate)) > 1e-6)
				break;
	} 

	printf ("%.7lf\n", best);

}
int main()
{
	int k; 
	scanf("%d", &k);

	for(int i=1; i <=k; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}

}
