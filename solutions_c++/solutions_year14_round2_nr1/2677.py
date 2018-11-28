#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	ifstream in("1A.in");
	ofstream out("1A.out");

	int N, T;
	in >> T;

	for (int i = 1; i <= T; i++)
	{
		in >> N;
		vector<string> str(N);

		for (auto &e : str)
			in >> e;

		vector<vector<pair<char, int>>> ss(N);

		for (int j = 0; j < str.size(); j++)
		{
			int c = 0;
			char pre = str[j][0];
			for (int m = 0; m < str[j].size(); m++)
			{
				if (pre != str[j][m])
				{
					ss[j].push_back({ pre, c });
					pre = str[j][m];
					c = 0;
				}
				c++;
			}
			ss[j].push_back({ pre, c });
		}

		bool suc = true;
		int count = 0;
		int index = 0;

		for (int m = 1; m < ss.size(); m++)
		{
			if (ss[0].size() != ss[m].size())
			{
				suc = false;
				break;
			}
		}

		while (suc && index < ss[0].size())
		{
			char c = ss[0][index].first;
			for (int m = 1; m < ss.size(); m++)
			{
				if (c != ss[m][index].first)
				{
					suc = false;
					break;
				}
			}

			int t = 0;
			for (int m = 0; m < ss.size(); m++)
				t += ss[m][index].second;

			int a = ((float)t / ss.size() + 0.5f);

			for (int m = 0; m < ss.size(); m++)
				count += abs(ss[m][index].second - a);

			index++;
		}

		out << "Case #" << i << ": ";
		if (!suc)
			out << "Fegla Won" << endl;
		else
			out << count << endl;

	}

	in.close();
	out.close();

	return 0;
}