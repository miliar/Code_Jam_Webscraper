#include <iostream>
#include <string>
#include <algorithm>
#include <queue>
#include <vector>
#include <fstream>
using namespace std;
int main()
{
	ifstream fin("B-large.in");
	ofstream fout("output.txt");
	int T;
	fin>> T;
	for (int TT = 1; TT != T+1; TT++)
	{
		int D, minMinute=0x0fffffff;
		int maxAi = 0;
		fin >> D;
		vector<int> a(D);
		for (int i = 0; i != D; i++)
		{
			fin >> a[i];
			maxAi = max<int>(maxAi, a[i]);
		}
		for (int i = 1; i <= maxAi; i++)
		{
			int sum = 0;
			for (int j = 0; j != D; j++)
			{
				if (a[j]>i)
				{
					if (a[j] % i) sum += a[j] / i;
					else sum += a[j] / i - 1;
				}
			}
			minMinute = min<int>(minMinute, sum+i);
		}		
		fout << "Case #" << TT << ": " << minMinute << endl;
	} 
}