#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

ifstream fin("B-large.in");
ofstream fout("output.txt");

// #define fin cin
// #define fout cout

int main(int argc, char const *argv[])
{
	ios::sync_with_stdio(false);
	int t;
	fin>>t;
	int u = 0;
	while(u++ < t)
	{
		int d;
		fin>>d;
		vector<int> vec(d);
		int pMax = 0;
		for (int i = 0; i < d; ++i)
		{
			fin>>vec[i];
			pMax = max(pMax, vec[i]);
		}
		int sol = 1e9;
		for (int i = 1; i <= pMax; ++i)
		{
			int res = i;
			for (int j = 0; j < d; ++j)
			{
				if(vec[j] > i)res += (vec[j] - 1) / i;
			}
			sol = min(sol, res);
		}
		fout<<"Case #"<<u<<": "<<sol<<endl;
		cerr<<"Done\n";
	}
	return 0;
}