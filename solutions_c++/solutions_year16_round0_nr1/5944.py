#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("a.in");
ofstream fout("a.out");

int main()
{
	int T;
	long long n;
	fin >> T;
	for (int i = 1; i <= T; i++)
	{
		fin >> n;
		fout << "Case #" << i << ": ";
		if (n == 0) fout << "INSOMNIA\n";
		else
		{
			int mark = 0;
			int j = 1;
			long long m = j * n;
			while (m > 0)
			{
				while (m > 0)		
				{
					int d = m % 10;
					m = m / 10;
					mark = mark | (1 << d);
				}
				if (mark == 1023)
				{
					fout << j * n << endl;
					break;
				}
				j++;
				m = j * n;
			}
		}
	}
	return 0;
}