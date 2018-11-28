#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <algorithm>
#include <iostream>
#include <cstdlib>



using namespace std;


int commonCard(vector<int> &v, set<int> &s, int &ans)
{
	int count = 0;
	for (unsigned int i = 0; i < v.size(); i++)
	{
		if (s.find(v[i]) != s.end()) {
			count++;
			ans = v[i];
		}
	}
	return count;
}

int main()
{

	int T;

	ifstream fin("C:\\weilin\\Competition\\GCJ2014Qualification\\GCJ2014Qualification\\A-small-attempt0.in");
	ofstream fout("output.txt");

	fin >> T;

	long long total = 0;


	for (int i = 0; i < T; i++)
	{
		int r1, r2;
		fin >> r1;

		vector<int> v[4];
		set<int> s[4];

		for (int j = 0; j < 4; j++)
		{
			int card = 0;
			for (int k = 0; k < 4; k++)
			{
				fin >> card;
				v[j].push_back(card);
			}
		}
		fin >> r2;

		for (int j = 0; j < 4; j++)
		{
			int card = 0;
			for (int k = 0; k < 4; k++)
			{
				fin >> card;
				s[j].insert(card);
			}
		}

		int ans = 0;
		int count = commonCard(v[r1-1], s[r2-1], ans);
		if (count == 0)
		{
			fout << "Case #" << i + 1 << ": " << "Volunteer cheated!" << endl;
		}
		else if (count == 1)
		{
			fout << "Case #" << i + 1 << ": " << ans << endl;
		}
		else if (count > 1)
		{
			fout << "Case #" << i + 1 << ": " << "Bad magician!" << endl;
		}

	}
	return 0;
}