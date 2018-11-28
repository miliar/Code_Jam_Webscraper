#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;

int main()
{
	ofstream fout;
	fout.open ("results.txt");
	int cases, test;
	double c, f, x;
	double rate;
	double min, newMin;

	cin>>cases;
	test = 1;

	while(test <= cases)
	{
		rate = 2.0;
		cin>>c>>f>>x;
		min = 0;
		newMin = -1;

		while (newMin != min)
		{
			newMin = x/rate;

			if(c/rate + x/(rate + f) < newMin)
			{
				min += c/rate;
				newMin = x/(rate + f);
				rate += f;
			}
			else
			{
				min += newMin;
				break;
			}
		}

		fout<<"Case #"<<test<<": "<<fixed<<showpoint<<setprecision(7)<<min<<endl;

		test++;
	}


	return 0;
}
