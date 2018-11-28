
#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <map>
#include <algorithm>
#include <string>
#include <queue>
#include <climits>

using namespace std;

#define ALL(v) (v).begin(), (v).end()

vector<string> alfabet = {"A",	"B",	"C",	"D",	"E",	"F",	"G",	"H",	"I",	"J",	"K",	"L",	"M",	"N",	"O",	"P",	"Q",	"R",	"S",	"T",	"U",	"V",	"W",	"X",	"Y",	"Z"};

int main(int argc, char *argv[])
{
	ifstream fin;
	fin.open(argv[1]);

	int T; fin >> T;

	for (int i = 1; i <= T; i++)
	{
		int P; fin >> P;
		vector<pair<int, int>> ptrs;
		int total = 0;
		for (int j = 0; j < P; j++)
		{
			int v;
			fin >> v;
			ptrs.push_back({j, v});
			total += v;
		}

		cout << "Case #" << i << ": ";
		int remP = P;
		while (total != 0)
		{
			sort(ALL(ptrs), [] (pair<int, int> & x, pair<int, int> & y) { return x.second > y.second; });
			int fts = -1;
			int sec = -1;
			for (int j = 0; j < ptrs.size(); j++)
			{
				if (ptrs[j].second == 0) continue;
				if (j == 0 && ptrs[j].second == 1 && remP == 3)
				{
					total -= 1;
					ptrs[j].second -= 1;
					if (ptrs[j].second == 0) remP--;
					cout << alfabet[ptrs[j].first] << " ";
					break;
				}
				if (ptrs[j].second * 2 >= total)
				{
					if (ptrs[j].second >= 2 && remP > 2 && fts == -1)
					{
						fts = ptrs[j].first;
						sec = ptrs[j].first;
						total -= 2;
						ptrs[j].second -= 2;
						if (ptrs[j].second == 0) remP--;
					}
					else
					{
						if (fts == -1) fts = ptrs[j].first;
						else sec = ptrs[j].first;
						total -= 1;
						ptrs[j].second -= 1;
						if (ptrs[j].second == 0) remP--;
					}
				}
				else
				{
					if (fts == -1) fts = ptrs[j].first;
					else sec = ptrs[j].first;
					total -= 1;
					ptrs[j].second -= 1;
					if (ptrs[j].second == 0) remP--;
				}
				if (fts != -1 && sec != -1)
				{
					cout << alfabet[fts] << alfabet[sec];
					if (total != 0) cout << " ";
					break;
				}

			}
		}
		cout << endl;
	}
}
