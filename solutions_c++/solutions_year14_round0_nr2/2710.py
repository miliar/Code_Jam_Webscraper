#include <iostream>
#include <fstream>
#include <limits>
#include <iomanip>
namespace
{
	const double MaxDouble = std::numeric_limits<double>::infinity();
}

using namespace std;


ofstream output("D:\\out.txt");

int main()
{
	ifstream file;
	file.open("D:\\in.txt");
	int counter;
	char in[8];
	file >> in;
	counter = atoi(in);
	int testnum = 1;
	double basesofar = 0, total = MaxDouble, newTotal = 0;
	cout.precision(8);
	while (!file.eof())
	{
	
		double C, F, R = 2, X, number, base;
		file >> C;
		file >> F;
		file >> X;
		number = X / C;
		total = MaxDouble;
		basesofar = 0;
		while (1)
		{
			base = C / R;
			newTotal = base*number + basesofar;
			if (newTotal < total)
				total = newTotal;
			else{ break; }
			R += F;
			basesofar += base;
		}

		output << "Case #" << testnum << ": " << fixed << total << endl;

		testnum++;
		if (counter+1 == testnum)
			break;
	}
	return 0;
}