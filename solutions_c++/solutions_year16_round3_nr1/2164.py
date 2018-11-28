#include <fstream>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <queue>
#include <cstdint>
#include <unordered_map>
#include <map>
#include <unordered_set>
#include <functional>

using namespace std;
typedef long long ll;

struct sort_pred {
	bool operator()(const std::pair<char, int> &left, const std::pair<char, int> &right) {
		return left.second > right.second;
	}
};

int main()
{
	string fileName = "input.txt";
	ifstream file(fileName.c_str());

	ofstream outputfile;
	outputfile.open("Output.txt");

	string line, S;
	int T = 0, N;
	int alph[30];
	

	if (file.is_open())
	{
		getline(file, line);
		T = stoi(line);

		for (int i = 0; i < T; ++i)
		{
			for (size_t j = 0; j < 30; j++)
			{
				alph[j] = 0;
			}

			vector<pair<char, int>> al;
			int count = 0;
			char x, re, re1;

			file >> N;
			
			for (size_t j = 0; j < N; j++)
			{
				file >> alph[j];
				x = 'A' + j;
				al.push_back(make_pair(x, alph[j]));
				count += alph[j];
			}
			outputfile << "Case #" << i + 1 << ": ";

			while (count > 0)
			{
				std::sort(al.begin(), al.end(), sort_pred());

				if (count == 1)
				{
					re = al.begin()->first;

					al[0].second -= 1;
					count -= 1;
					
					outputfile << re ;
				}
				else if (count == 2)
				{
					if (al.begin()->second == 2)
					{
						re = al[0].first;

						al[0].second -= 2;
						count -= 2;

						outputfile << re << re ;
					}
					if (al.begin()->second == 1)
					{
						re = al[0].first;
						re1 = al[1].first;

						al[0].second -= 1;
						al[1].second -= 1;
						count -= 2;

						outputfile << re << re1;
					}
				}
				else if (count == 3)
				{
					re = al[0].first;

					al[0].second -= 1;
					count -= 1;

					outputfile << re << " ";
				}
				else if (al.begin()->second >= 2)
				{
					vector<pair<char, int>> tempal = al;
					re = al[0].first;

					al[0].second -= 2;
					count -= 2;

					std::sort(al.begin(), al.end(), sort_pred());

					if (al[0].second * 2 <= count)
					{
						outputfile << re << re << " ";
					}
					else
					{
						al = tempal;
						count += 2;

						if (al[0].second >= 1 && al[1].second >= 1)
						{
							re = al[0].first;
							re1 = al[1].first;

							al[0].second -= 1;
							al[1].second -= 1;
							count -= 2;

							outputfile << re << re1 << " ";
						}
					}
				}
				else if (al[0].second >= 1 && al[1].second >= 1)
				{
					re = al[0].first;
					re1 = al[1].first;

					al[0].second -= 1;
					al[1].second -= 1;
					count -= 2;

					outputfile << re << re1 << " ";
				}
			}

			
			outputfile << endl;
		}
	}

	file.close();

	outputfile.close();

	return 0;
}