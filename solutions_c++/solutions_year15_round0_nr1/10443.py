#include <fstream>
using namespace std;

int main()
{
	ifstream fin("A-small-attempt0.in");
	ofstream fout("output.out");
	int t;
	fin >> t;
	char mas[1002];
	for (int i = 1; i <= t ; i++)
	{
		int Smax;
		fin >> Smax;
		int kol = 0, invite = 0;
		char c;
		fin.get(c);
		for (int j = 0; j <= Smax; j++)
		{
			fin.get(mas[j]);
		}
		mas[Smax + 1] = '\0';
		for (int j = 0; j <= Smax; j++)
		{
			if ((int)mas[j] - (int)'0' != 0)
			{
				if (kol >= j)
				{
					kol += (int)mas[j] - (int)'0';
				}
				else
				{
					invite += j - kol;
					kol += invite + (int)mas[j] - (int)'0';
				}
			}
		}
		fout << "Case #" << i << ": " << invite << endl;
	}
	return 0;
}

