#pragma warning(disable : 4996)  
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
		int ans = 0,now = 0;
		fin >> n;
		for (int i = 0; i <= n; i++)
		{
			if (now < i)
			{
				ans++;
				now++;
			}
			char numchar;
			fin >> numchar;
			int num = numchar - '0';
			now += num;
		}
		fout << "Case #" << Case << ": " << ans << endl;
	}
	fin.close();
	fout.close();
	return 0;
}