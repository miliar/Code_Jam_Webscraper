#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
	int t;
	cin>>t;
	
	for(int ti = 0; ti < t; ti++)
	{
		double c; // Cost of cookie farm
		double f; // cps of one farm
		double x; // needed cookies of commission
		double cps = 2; // my cookies per second
		//double cookies = 0; 
		double time = 0; // time for answer
		cin>>c>>f>>x;
		
		while(true)
		{
			double a; // Time to build new farm
			double b; // Time to done the commission
			double cc; // Time to build new farm and then commision
			
			
			a = (c) / cps;
			b = (x ) / cps;
			cc = a + x / (cps+f);
			
			if(b < cc)
			{
				time += b;
				break;
			} else
			{
				time += a;
				cps += f;
			}
		}
		cout<<"Case #"<<ti+1<<": "<<fixed<<setprecision(7)<<time<<endl;
		
	}
	return 0;
}
