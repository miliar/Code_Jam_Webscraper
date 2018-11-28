# include <iostream>
#include <cstdio>

using namespace std;

double cookieRate;
double TimeTaken(double X)
{
	return X/cookieRate;
}
double ClickCookies(double C, double F, double X)
{
	double answer = 0;
	cookieRate = 2;
	while(true)
	{
		double timeTaken = TimeTaken(X);
		double timeToBuyFarm = C/cookieRate;
		cookieRate += F;
		double newTime = timeToBuyFarm + TimeTaken(X);
		//cout<<timeTaken<<" "<<newTime<<endl;
		if(timeTaken < newTime)
		{
			return (answer + timeTaken);
		}
		else
		{
			answer += timeToBuyFarm;
		}
	}
}

int main()
{
	int T, i;
	cin>>T;
	for(i=1; i<=T; i++)
	{
		double C, F, X;
		cin>>C>>F>>X;
		double answer = ClickCookies(C, F, X);
		printf("Case #%d: %.7f\n", i, answer);
	}
	return 0;
}
