#include <vector>
#include <string>
#include <iostream>
#include <fstream>

using namespace std;

bool input(int x)
{
	if (x > pow(10,6) || x == 0)
		return false;
	return true;
	
}

void main()
{
	unsigned int T = 100, N, i, x = 1, k = 0;

	ifstream ifile("A-large.in");
	ofstream ofile("A-small-attempt0.out");


	ifile >> T;

	char digits[10 + 1] = "x123456789";
		
	for (unsigned int nCase = 1; nCase <= T; nCase++)
	{		
		ifile >> N;

		strcpy_s(digits, "x123456789");
		i = 1;

		while (strcmp(digits, "0000000000") && input(N) && i < 10000)
		{
			x = N * i;

			while (x / 10 >= 0 && x > 0)
			{
				digits[x % 10] = '0';
				x = x / 10;
				
			}
			i++;

		}
		if (input(N) && i < 10000)
		{
			ofile << "Case #" << nCase << ": " << N * (i - 1) << endl;
		}
		else
			ofile << "Case #" << nCase << ": INSOMNIA" << endl;
	}

	ofile.close();
	ifile.close();
}