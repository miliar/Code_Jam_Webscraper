#ifndef MAX
#define MAX 1E6
#endif

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <math.h>
using namespace std;

int main(int argc, char const *argv[])
{
	ifstream infile("A-large.in");
	int T;
	if (!(infile >> T))
	{
		cerr << "Empty file!" << endl;
		return 1;
	}
	ofstream outfile("A-large.out");
	int digits[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
	for (int i = 0; i < T; i++)
	{
		int N;
		if (infile >> N && N >= 0 && N <= MAX)
		{
			outfile << "Case #" << i + 1 << ": ";
			if (N == 0)
			{
				outfile << "INSOMNIA" << endl;
				continue;
			}
			else
			{
				int Nk = N;
				bool sleep = false;
				set<int> digitset (digits, digits + 10);
				while (!sleep)
				{
					int Nk_bak = Nk;
					do
					{
						digitset.erase(Nk % 10);
						Nk /= 10;
					}
					while (Nk);
					if (digitset.empty())
					{
						sleep = true;
						outfile << Nk_bak << endl;
					}
					else
					{
						Nk = Nk_bak + N;
					}
				}
			}
			
		}
		else
		{
			cerr << "Invalid file!" << endl;
			return 1;
		}
	}
	return 0;
}