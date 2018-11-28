#include <iostream>       // std::cout
#include <stdio.h>
#include <iomanip>
using namespace std;
typedef unsigned int uint;
double caltime(double c,double f,double x,double rate)
{

	uint uic= 0;
	double time = 0,time1 = 0, time2 = 0;
	if(x-c < 0)
	{
		time += x/rate;
		return time;
	}
	while((((x+c)/(rate+f) - (x/rate)) < 0))
	{
		time += c/rate;
		rate += f;
		uic++;
	}

		rate = rate-f;
		time += (x-c)/rate;


	return time;
	
/*	time = c/rate;
	
	time1 = caltime(c,f,x,rate+f);

	time2 = caltime(c,f,x-c,rate);
	if(time1 - time2 > 0)
	{
		time += time2;
	}
	else
	{
		time += time1;
	}
	return time;

/*	uint uinum;
	double time = 0,time1 = 0, time2 = 0;
	if(x-c < 0.00000000)
	{
		time = x/rate;
		return time;
	}
	if(((x+c)/(rate+f) - (x/rate)) > 0.00000000)
	{
		time = x/rate;
		return time;
	}
	
	
	time = c/rate;
	
	time1 = caltime(c,f,x,rate+f);

	time2 = caltime(c,f,x-c,rate);
	if(time1 - time2 > 0.00000000)
	{
		time += time2;
	}
	else
	{
		time += time1;
	}
	return time;*/
}

int main ()
{
	uint test_cases = 0;
  	cin >> test_cases;

	double C,F,X,ans,rate;

  	for (uint i=1;i<=test_cases;i++) 
  	{	
		cin >> C >> F >> X;
		rate= 2;		
		ans = caltime(C,F,X,rate);
		cout << std::fixed;
		cout << "Case #" << i << ": " << std::setprecision(7) << ans << endl;
		//printf("%.7f\n",ans);

  	}
  return 0;
}
