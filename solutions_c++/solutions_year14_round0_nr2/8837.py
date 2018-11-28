#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>

using namespace std;

typedef unsigned int u32;

double timeatnext(vector<double> const & farmtimes, double C, double F)
{
	return (farmtimes.empty() ? 0 : *farmtimes.rbegin()) + C / (2 + F * farmtimes.size());
}

int main(int, char **)
{
	ifstream in;
	ofstream out;

	in.open("input.in");
	out.open("output.out");

	u32 T;
	in >> T;
	++T;

	for (u32 i = 1; i < T; ++i)
	{
		double C, F, X;
		in >> C >> F >> X;	
	
		vector<double> timetofarm;
		double time;
		while ((time = timeatnext(timetofarm, C, F)) + X / (2 + F * (timetofarm.size() + 1)) < timeatnext(timetofarm, X, F))
		{
			timetofarm.push_back(time);
		}
		cout << "Case #" << i << ": " << std::setprecision(9) << timeatnext(timetofarm, X, F) << endl;
		out << "Case #" << i << ": " << std::setprecision(9) << timeatnext(timetofarm, X, F) << endl;
	}

	out.close();
	in.close();
	getchar();
	return 0;
}