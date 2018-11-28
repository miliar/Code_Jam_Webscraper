#pragma warning(disable : 4996)  
#include <vector>
#include <iostream>
#include <algorithm>
#include <fstream>
using namespace std;

int main()
{
	ifstream fin("1.in");
	int t;
	fin >> t;
	ofstream fout("1.out");
	for (int Case = 1; Case <= t; Case++)
	{
		int n;
		fin >> n;
		int maxp = 0;
		vector<int> p(n);
		for (int i = 0; i < n; i++)
		{
			fin >> p[i];
			if (p[i]>maxp)
				maxp = p[i];
		}
		int ans = maxp;
		for (int i = 1; i < maxp; i++)
		{
			int now = i;
			for (int j = 0; j < n; j++)
			{
				now += (p[j] - 1) / i;
			}
			if (now < ans) ans = now;
		}
		fout << "Case #" << Case << ": " << ans << endl;
	}
	fin.close();
	fout.close();
	return 0;
}