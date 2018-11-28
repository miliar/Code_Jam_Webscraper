#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;
void main()
{
	ifstream in("B-large.in");
	ofstream out("output.txt");
	double c, f, x;
	int cases;
	double rate = 2;
	in >> cases;
	in.ignore();
	for (int i = 0; i < cases; i++)
	{
		double time = 0;
		in >> c;
		in >> f;
		in >> x;
		while (((c/rate) + (x/(rate + f)) < (x/rate)))
		{
			time = time + (c / rate);
			rate = rate + f;
		}
		time = time + (x / rate);
		out << fixed << setprecision(7);
		out << "Case #" << i + 1 << ": " << time << "\n";
		rate = 2;
	}
}