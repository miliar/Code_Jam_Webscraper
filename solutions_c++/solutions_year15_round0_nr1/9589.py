#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	ifstream infile;
	ofstream outfile;

	infile.open("A-large.in");
	outfile.open("output.txt");

	int t, smax;
	string shy;
	int result[100], frnd = 0, ppl,j;
	char n;

	infile >> t;
	infile.ignore(100, '\n');

	for (int i = 0; i < t; i++)
	{
		ppl = frnd = 0;
		infile >> smax >> shy;
		n = shy[0];

		ppl = atoi(&n);
		j = 1;

		do
		{
			while (ppl < j)
			{
				ppl++;
				frnd++;
			}
			n = shy[j];
			ppl += atoi(&n);

			j++;
		} while (j <= smax);

		result[i] = frnd;
	}

	for (int i = 0; i < t; i++)
	{
		outfile << "Case #" << i + 1 << ": " << result[i] << endl;
	}

}