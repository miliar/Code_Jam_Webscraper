#include<iostream>
#include<fstream>

using namespace std;
int main()
{
	cout.precision(7);
	int cases,test;
	long double c,f,x,sum,factor; 
	cin>>cases;
	test = cases;
	while(cases)
	{
		cin>>c>>f>>x;
		factor = 2.0;
		sum = 0.0;
		for(;;)
		{
			if((c/factor)+(x/(factor+f)) < x/factor )
			{
				sum = double(double(sum) + double(c/factor));
				factor = double(double(factor) + double(f));
			}
			else
			{
				sum = double(double(sum) + double(x/factor));
				break;	
			}	
			
		}
	
		cout<<"Case #"<<test-cases+1<<": "<<fixed<<double(sum)<<endl;;
		
		
		cases--;	
	}



cin.get();
cin.get();
return 0;
}
