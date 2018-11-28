#include <fstream>
#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

#define DEBUG 1

int main()
{
	ofstream output;
	ifstream input ("B-small-attempt0.in");
	output.open("B-small-attempt0.out");

	int t;

	input >> t;

	for (int i=0; i<t; i++)
	{
		output << "Case #"<<i+1<<": ";
		double c, f, x;

		input>>c>>f>>x;

#if DEBUG
		cout <<c<<" "<<f<<" "<<x<<endl;
#endif

		int n  = ceil( (f*x - 2*c - f*c)/(f*c) );
		if (n < 0)
			n = 0;

		double time = 0.0;

		for (int j=0; j < n; j++)
		{
			time += c / (2 + f * j);
		}

		time += x / (2 + n * f);

		output<<fixed<<setprecision(7)<<time<<endl;
#if DEBUG
		cout<<time<<endl;
#endif
	}

	return 0;
}





		


