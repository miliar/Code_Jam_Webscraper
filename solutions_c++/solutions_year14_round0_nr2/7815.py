#include <iostream>
#include <iomanip>

using namespace std;

void cookieClicker()
{
	int tests;
	cin>>tests;
	for(int n=1; n<=tests; ++n)
	{
		double curr = 0.0;
		double r = 2.0;
		
		double C, F, X;
		cin>>C>>F>>X;
		
		double secs = X/r;
		while(1)
		{
			curr += C/r;
			r += F;
			double temp = (curr + X/r);
			if(temp < secs)
				secs = temp;
			else
				break;
		}
		
		cout<<"Case #"<<n<<": "<<fixed<<setprecision(7)<<secs<<"\n";
	}
}