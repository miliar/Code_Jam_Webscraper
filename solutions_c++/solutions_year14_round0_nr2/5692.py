#include<iostream>
#include <iomanip> 
#include <fstream>
using namespace std;

int main()
{
	int test,z;
	double c,f,x,i=2.0,x1,x2;
	long double ans;
	ofstream myfile;
		myfile.open ("2.txt");
	cin >> test;
	z = test;
	while(test)
	{ 
		i = 2.0;
		ans = 0.0;
		cin >> c >> f >> x;
		while(i)
		{
			x1 = x/i;
			x2 = c/i + x/(i+f);
			if(x1 < x2)
			{
				ans += x1;
				break;
			}
			else
			{
				ans += (c/i);
				i=i+f;
			}
		}
		myfile << "Case #"<<z-(test-1)<<": "<<setprecision(10) <<ans<<"\n";
		test--;
	}
	return 0;
}
			
			
			
			
