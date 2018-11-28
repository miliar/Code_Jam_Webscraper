#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream fin("A-small-attempt0.in");
	ofstream fout("A-small-attempt0.out");
	int itest, ntest;
	fin >> ntest;
	for (itest = 0; ++itest <= ntest;)
	{
		int n, res = 0, sum = 0;
		char num[65536];
		fin >> n >> num;
		for (int i = 0; i <= n; ++i)
		{
			if (sum < i && num[i] != '0')
			{
				res += i - sum;
				sum += res;
			}
			sum += num[i] & 15;
		}
		fout << "Case #" << itest << ": " << res << endl;
	}
	return 0;
}
