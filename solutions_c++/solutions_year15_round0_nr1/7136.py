#include <iostream>
#include <string>
#include <fstream>

using namespace std;


int main()
{	
	ifstream fin("A-large.in");
	ofstream fout("r.out");
	int num;
	fin >> num;
	for (int i = 0; i < num; i++)
	{
		int cdf[1001] = {0};
		int high;
		string s;
		fin >> high >> s;
		int sum = 0;
		if (high == 0)
		{
			fout << "Case #" << i+1 << ": 0" << endl;
			continue;
		}
		cdf[0] = s[0] - '0';
		for (int j = 1; j <= high; j++)
		{
			int temp = 0;
			if (j > cdf[j - 1])
				temp = (j - cdf[j - 1]);
			sum += temp;
			cdf[j] = cdf[j - 1] + temp + (s[j] - '0');
		}
		fout << "Case #" << i+1 << ": " << sum << endl;
	}
	fin.close();
	fout.close();
	return 0;
}