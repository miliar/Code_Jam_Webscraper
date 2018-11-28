#include <fstream>
#include <iostream>


bool isPal (long);


int main (int argc, char ** argv)
{

	using namespace std;

	ifstream infile (argv[1]);
	ofstream outfile ("output_file.txt");

	if (infile.is_open() && outfile.is_open())
	{

		int nCases;
		infile >> nCases;

		for (int casenum = 1; casenum <= nCases; ++casenum)
		{

			long min, max, sqrmin, sqrmax, nfs = 0;
			infile >> sqrmin >> sqrmax;
			for (min = 1; min * min < sqrmin; ++min);
			for (max = min; max * max <= sqrmax; ++max);

			for (long curnum = min; curnum < max; ++curnum)
			{

				if (isPal(curnum) && isPal(curnum * curnum))
				{
					++nfs;
				}

			}

			outfile << "Case #" << casenum << ": " << nfs << endl;

		}

		infile.close();
		outfile.close();

		return 0;

	}
	else
	{

		cerr << "File open error, try again" << endl;

		infile.close();
		outfile.close();

		return -1;

	}

}


bool isPal (long num)
{

	static char isPalMem[2147483648];

	if (isPalMem[num - 1] == 0)
	{

		long num_ = num;
		long mun = 0;

		while (num_ > 0)
		{

			mun *= 10;
			mun += num_ % 10;
			num_ /= 10;

		}

		isPalMem[num - 1] = ((num == mun) ? 2 : 1);

	}

	return isPalMem[num - 1] - 1;

}
