#include <fstream>
using namespace std;
ofstream fout("date.out");
ifstream fin("date.in");
long long int ap[10];
int main()
{
	long long int n, T;
	long long int i, j, k,count;
	bool gasit;
	fin >> T;
	for (long long int test = 1; test <= T; test++)
	{
		fin >> n;
		if (n)
		{
			for (i = 0; i <= 9; i++)
				ap[i] = 0;
			count = 0; //resetare 
			gasit = 0;
			for (j = 1; j <= 200000; j++)
			{
				long long int numar = j * n;
				while (numar)
				{
					if (ap[numar % 10] == 0)
						count++;
					ap[numar % 10] = 1;
					numar /= 10;
				}
				if (count == 10)
				{
					fout << "Case #" << test << ": " << j*n << '\n';
					gasit = 1;
					break;
				}

			}
			if (!gasit)
				fout << "Case #" << test << ": INSOMNIA" << '\n';
		}
		else
		{
			fout << "Case #" << test << ": INSOMNIA" << '\n';
		}
	}
}