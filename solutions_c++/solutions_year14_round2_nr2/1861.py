#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <algorithm>
#include <iostream>
#include <cstdlib>


using namespace std;

int main()
{

	int T;

	ifstream fin("C:\\weilin\\Competition\\GCJ20141A\\GCJ20141A\\B-small-attempt0.in");
	ofstream fout("output.txt");

	fin >> T;

	long long total = 0;

	for (int i = 0; i < T; i++)
	{
		int A, B, K;
		fin >> A >> B >> K;
		total = 0;
		set<int> st;
		for (int m = 0; m < A; m++)
		for (int j = 0; j < B; j++)
		{
			long long n = m & j;
			if (n < K)
			{
				
				    total++;
			}
		}
	

		fout << "Case #" << i + 1 << ": " << total << endl;

	}
	return 0;
} 