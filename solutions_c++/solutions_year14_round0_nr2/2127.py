#include<iostream>
#include<fstream>

using namespace std;

double writeSummary(double c, double f, double x);

int main ()
{
	ifstream myfileIn;
	myfileIn.open ("C:/stack/oldstuff/Computer Languages/Google/sample.txt");
	if(!myfileIn.good())
	{
		return 0;
	}
	cout.precision(7);
	int cases = 0;
	myfileIn >> cases;
	
	ofstream myfileOut;
	myfileOut.open ("C:/stack/oldstuff/Computer Languages/Google/out.txt");
	for(int i = 0; i < cases; i++)
	{
		double c;
		double f;
		double x;
		myfileIn >> c;
		myfileIn >> f;
		myfileIn >> x;
		double ans;
		ans = writeSummary(c, f, x);
		cout << fixed << showpoint << "Case #" << (i+1) << ": " << ans << endl;
		myfileOut << fixed << showpoint << "Case #" << (i+1) << ": " << ans << endl;
	}

	return 0;
}

double writeSummary(double c, double f, double x)
{
	double perSec = 2.0;
	double time = 0.0;
	double timeToEnd = (x/perSec);
	double newTime = ((x/(perSec+f))+(c/perSec));
	while(timeToEnd > newTime)
	{
		time += (c/perSec);
		perSec += f;
		timeToEnd = (x/perSec);
		newTime = ((x/(perSec+f))+(c/perSec));
	}
	return (time+timeToEnd);
}