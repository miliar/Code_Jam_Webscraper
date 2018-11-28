#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;

int main(int argc, char** argv)
{
	ifstream in(argv[1]);
	ofstream out(argv[2]);
	if (in.is_open() && out.is_open())
	{
		int n = 26;
		int m = 10;
		pair<string, int> dict[m] = {{"ZERO", 0}, {"TWO", 2}, {"SIX", 6}, {"FOUR", 4}, {"EIGHT", 8}, {"FIVE", 5}, {"SEVEN", 7}, {"THREE", 3}, {"NINE", 9}, {"ONE", 1}};

		int ts; in >> ts;
		for (int t = 1; t <= ts; ++t)
		{
			string s; in >> s;
			int data[n] = {0};
			for (const auto& ch : s) ++data[ch - 'A'];
			vector<int> res;
			
			for (int i = 0; i < m; ++i)
			{
				bool ok = true;
				while (ok)
				{
					int used[n] = {0};
					for (const auto& ch : dict[i].first)
					{
						if (data[ch - 'A'] == 0) ok = false;
						else
						{
							--data[ch - 'A'];
							++used[ch - 'A'];
						}
					}
					if (ok) res.push_back(dict[i].second);
					else for (int k = 0; k < n; ++k) data[k] += used[k];
				}
			}
			sort(res.begin(), res.end());
			out << "Case #" << t << ": ";
			for (const auto& r : res) out << r;
			out << "\n";
		}
	}
	else
	{
		cerr << "failed to open file\n";
	}
	return 0;
}
