#include <vector>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;
const int INF = 2147483647;

int main()
{
	int t;
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	fin >> t;
	for (int times = 1; times <= t; times++)
	{
		string s;
		fin >> s;
		int l = s.size();
		vector<int> allneg(l, INF), allpos(l, INF);
		
		if (s[0] == '+')
		{
			allneg[0] = 1;
			allpos[0] = 0;
		}
		else
		{
			allneg[0] = 0;
			allpos[0] = 1;
		}
		for (int k = 1; k < l; k++)
		{
			if (s[k] == '+')
			{
				allpos[k] = allpos[k - 1];
				allneg[k] = allpos[k - 1] + 1;
			}
			else
			{
				allpos[k] = allneg[k - 1] + 1;
				allneg[k] = allneg[k - 1];
			}
		}
		fout << "Case #" << times << ": " << allpos[l - 1] << endl;
	}
	return 0;
}