#include <vector>
#include <tuple>
#include <set>
#include <algorithm>
#include <math.h>
#include <iomanip>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;
int devide(vector<int> diners)
{
	int max = 0;
	int ind = 0;
	for (int j = 0; j < diners.size(); j++)
	{
		if (diners[j] > max){
			max = diners[j];
			ind = j;
		}
	}
	if (max < 4) return max;
	int res = max;
	for (int i = 2; i < 100; i++)
	{
		int part1 = (int)floor(max / i);
		if (part1 < 2) break;
		int part2 = max - part1;
		vector<int> newdiners(diners);
		newdiners[ind] = part1;
		newdiners.push_back(part2);
		int cur = devide(newdiners) + 1;
		if (cur < res)res = cur;
	}
	return res;
}
int main()
{
	ifstream fin;
	fin.open("B-small-attempt6.in");
	if (fin.is_open())
	{
		ofstream fout;
		fout.open("B-small-attempt6.out");
		int T;
		fin >> T;
		for (int i = 0; i < T; i++)
		{
			int N;
			fin >> N;
			vector<int> diners;
			for (int j = 0; j < N; j++)
			{
				int cur;
				fin >> cur;
				cout << cur<<" ";
				diners.push_back(cur);
			}
			cout << endl;
			int res = devide(diners);
			cout << "Case #" << i + 1 << ": " << res << endl;

			fout << "Case #" << i + 1 << ": " << res << endl;
		}
		fin.close();
		fout.close();
	}
	return 0;
}