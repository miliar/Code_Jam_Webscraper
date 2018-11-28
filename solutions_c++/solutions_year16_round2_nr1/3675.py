// Visual Studio 2015 Community Edition x64

#include <iostream>
#include <fstream>
#include <iomanip>
#include <vector>
#include <map>
#include <algorithm>
#include <string>

using namespace std;

#define ALL(v) (v).begin(), (v).end()

vector<string> numbers = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };

int main(int argc, char *argv[])
{
	ifstream fin;
	fin.open(argv[1]);
	string line;
	int T; fin >> T;
	getline(fin, line);
	for (int i = 1; i <= T; i++)
	{
		getline(fin, line);
		vector<pair<int, vector<char>>> digits;
		int sum = 0;
		for (int jj = 0; jj < line.length(); jj++)
		{
			digits.clear();
			vector<int> occupied(line.size(), 0);
			for (int j = 0; j < line.size(); j++)
			{
				if (occupied[j] != 0) continue;

				for (int j1 = 0; j1 < numbers.size(); j1++)
				{
					if (line[j] == numbers[j1][0])
					{
						vector<int> tmp_occupied;
						vector<int> tmp_occupiedPlc(line.size(), 0);
						pair<int, vector<char>> digit;
						digit.first = j1;
						digit.second.push_back(line[j]);
						tmp_occupied.push_back(j);
						tmp_occupiedPlc[j] = 1;
						int k;
						for (k = 1; k < numbers[j1].size(); k++)
						{
							int j2;
							for (j2 = 0; j2 < line.size(); j2++)
							{
								if (occupied[j2] != 0 || tmp_occupiedPlc[j2] != 0) continue;
								if (line[j2] == numbers[j1][k])
								{
									digit.second.push_back(line[j2]);
									tmp_occupied.push_back(j2);
									tmp_occupiedPlc[j2] = 1;
									break;
								}
							}
							if (j2 == line.size()) break;
						}
						if (k == numbers[j1].size())
						{
							for (auto index : tmp_occupied) occupied[index] = 1;
							digits.push_back(digit);
							break;
						}
					}
				}
			}
			sum = 0;
			for (auto gg : occupied) sum += gg;
			if (sum == line.size()) break;
			rotate(line.begin(), line.begin() + jj + 1, line.end());
		}
		
		sort(ALL(digits), [](auto & x, auto & y) { return x.first < y.first; });
		cout << "Case #" << i << ": ";
		for (auto & digit : digits) cout << digit.first;
		cout << endl;
	}

	return 0;
}

