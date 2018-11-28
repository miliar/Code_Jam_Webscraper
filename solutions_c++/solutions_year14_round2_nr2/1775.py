#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	int i, r;
	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int t;
	fin >> t;
	int a, b, k;

	for (int test = 0; test < t; test++)
	{
		fin >> a >> b >> k;
		int result = 0;

		for (i = 0; i < a; i++)
		{
			for (r = 0; r < b; r++)
			{
				if ((i & r) < k)
					result++;
			}
		}

		fout << "Case #" << (test + 1) << ": " << result << endl;
	}

	return 0;
}