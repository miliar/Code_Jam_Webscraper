#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;

void solve(double temp, double c, double f, double x, double &time)
{
	if ((x / (temp)) <= ((c / (temp)) + (x / (temp + f))))
	{
		time += x / temp;
		return;
	}
	else
	{
		time += c / temp;
		temp += f;
		solve(temp, c, f, x, time);
	}
}

int main() {


	ifstream in("input.txt");
	ofstream out("out.txt");
	int t = 0;
	in >> t;
	double c = 0, f = 0, x = 0, temp, time;

	for (int i = 0; i<t; i++)
	{

		in >> c >> f >> x;
		temp = 2; time = 0;

		solve(temp, c, f, x, time);

		out << "Case #";
		out << i + 1;
		out << ": ";
		out << std::fixed;
		out << std::setprecision(7);
		out << time << endl;
	}//end_for

	in.close();
	out.close();
	return 0;
}

