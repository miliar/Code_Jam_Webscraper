#include <fstream>
#include <iostream>
using namespace std;

int main()
{
	int n;
	ifstream fin("standing_case.txt");
	fin >> n;
	char S[1001];
	for (int i = 1; i <= n; ++i)
	{
		int len, count = 0, total = 0, diff;
		fin >> len; fin >> S;
		for (int j = 0; j <= len; ++j)
		{
			if(j <= total)
			{
				add:
				diff = ((int)S[j] - 48);
				//cout << "nrm " << diff << endl;
				total += diff;
			}
			else
			{
				diff = j - total;
				//cout << "diff " << diff << endl;
				total += diff;
				count += diff;
				goto add;
			}
		}

		cout << "Case #" << i << ": " << count << endl;
	}
}