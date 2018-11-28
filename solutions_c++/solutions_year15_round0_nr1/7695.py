#include<iostream>
#include <fstream>
#include<string>
using namespace std;

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("out-large.dat");

	int scale;
	fin >> scale;

	int S_max;
	string S;

	for (int i = 1;i<=scale; i++)
	{
		fin >> S_max;
		fin >> S;

		int stand = S[0] - 48;//standing people
		int friends = 0;//invited friends

		for (int k = 1; k <= S_max; k++)
		{
			if (stand < k)
			{
				friends += k - stand;
				stand = k + S[k] - 48;
			}
			else
				stand += S[k] - 48;
		}

		fout << "Case #" << i <<": "<< friends<<endl;
	}
	system("pause");
	return 0;
}