#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
using namespace std;

int main()
{
	ifstream fin("test.in");
	ofstream fout("test.out");

	int CASES;
	fin >> CASES;

	for (int CASENUMBER = 1; CASENUMBER <= CASES; CASENUMBER++)
	{
		vector<int> mushrooms;
		int ans1=0;
		int ans2 = 0;
		
		int N;
		fin >> N;
		for (int i = 0; i < N; i++)
		{
			int a;
			fin >> a;
			mushrooms.push_back(a);
		}

		for (int i = 0; i < mushrooms.size() - 1; i++)
		{
			if (mushrooms[i + 1] < mushrooms[i])
			{
				ans1 = ans1 + mushrooms[i] - mushrooms[i + 1];
			}
		}


		// find ans2;
		// first find min rate of eat
		
			// find max diff
		int maxdif = -1;
		for (int i = 0; i < mushrooms.size() - 1; i++)
		{
			if ((mushrooms[i] - mushrooms[i + 1]) > maxdif)
			{
				maxdif = (mushrooms[i] - mushrooms[i + 1]);
			}
		}
		double minrate = (double)maxdif / 10;

		// then go through
//		cout << "IM ON CASE " << CASENUMBER << endl;
	//	cout << "MINRATE IS " << minrate << endl;
		for (int i = 0; i < mushrooms.size() - 1; i++)
		{
			if (mushrooms[i] < 10 * minrate)
			{
				
				ans2 += mushrooms[i];
	//			cout << "ADDED" << mushrooms[i] << endl;
			}
			else
			{
				ans2 += minrate * 10;

		//		cout << "ADDED" << minrate * 10 << endl;
			}
		}
		
		fout << "Case #" << CASENUMBER << ": " << ans1 << " " << ans2 << endl;
	}
	cin.get();
}