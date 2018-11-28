#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iomanip>

using namespace std;

int main()
{
	ifstream infile;
	infile.open("B-large.in");

	ofstream e;
	e.open("r.txt");

	int t;
	infile >> t;

	double c, f, x;

	for(int b = 0; b < t ; b++)
	{
		e << "Case #" << b + 1 << ": ";
		infile >> c >> f >> x;

		vector<double> time;
		
		double fn = 0;
		double co = 2;
		double last = 0;


		time.push_back(x/co);
		fn++;
		co += f;
		time.push_back(c/(co-f) + x/co);
		last += c / (co-f);

		while(time[fn-1] > time[fn])
		{
			fn++;
			co += f;
			time.push_back(last + c/(co-f) + x/co);
			last += c / (co-f);
		}
		
		double small = time[0];
		for(size_t k = 0; k < time.size() - 1; k++)
		{
			if(small > time[k])
			{
				small = time[k];
			}
		}
		e << std::setprecision(14) << small << endl;
	}


	infile.close();
	e.close();
}