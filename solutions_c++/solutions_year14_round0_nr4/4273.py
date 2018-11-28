#include <map>
#include <fstream>
#include <math.h>
#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

int main()
{
	ifstream fin("war.in");
	ofstream fout("war.out");
	int N;
	fin >> N;
	for (int cases = 0; cases < N; cases++)
	{
		int r = cases + 1;
		fout << "Case #" << r << ": ";
		int blocks;
		fin >> blocks;
		vector<double> naomi(blocks);
		vector<double> ken(blocks);
		int a, b;
		vector<pair<double, bool>> total(2*blocks);
		for (int i = 0; i < blocks; i++)
		{
			fin >> naomi[i];
			total[i].first = naomi[i];
			total[i].second = false;
		}
		for (int i = 0; i < blocks; i++)
		{
			fin >> ken[i];
			total[blocks + i].first = ken[i];
			total[blocks + i].second = true;
		}
		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());
		sort(total.begin(), total.end());
		a = 0;
		int check = 0;
		for (int i = 0; i < (2*blocks); i++)
		{
			if (total[i].second == true) check++;
			else
			{
				if (check>0)
				{
					check--;
					a++;
				}
			}
		}
		check = 0;
		b = 0;
		for (int j = 0; j < (2 * blocks); j++)
		{
			int i = 2 * blocks - (j+1);
			if (total[i].second == true) check++;
			else
			{
				if (check>0)
				{
					check--;
				}
				else b++;
			}
		}
		fout << a << ' ' << b << endl;
	}
}