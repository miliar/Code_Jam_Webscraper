#include<fstream>
#include<iostream>
#include<iomanip>
using namespace::std;

int main()
{
	ifstream infile;
	infile.open("B-large.in");

	ofstream outfile;
	outfile.open("out.out");

	int t;
	infile >> t;
	outfile.precision(7);
	for(int l = 1; l <= t; l++)
	{
		long double c, f, x;
		infile >> c;
		infile >> f;
		infile >> x;
		//cout << c << " " << f << " " << x << " " << endl;
		long double wait_time = 0, time1 = 0, time2 = 0, total_time1 = 0, total_time = 0, previous = 999999999999999999, time = 0;
		long double production = 2;
		do
		{
			wait_time = x/production;
			time1 = c/production;
			production += f;
			time2 = x/production;
			time = time1 + time2;

			if(time < wait_time)
				total_time += time1;
			else total_time += wait_time;

		}while(time < wait_time);

		outfile << "Case #" << l << ": " << total_time << endl;

	}

	return 0;
}