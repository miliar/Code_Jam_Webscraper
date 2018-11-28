#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iterator>
#include <fstream>
#include <sstream>
#include <istream>
#include <unordered_map>

using namespace std;

vector<int> digitsContained(int number)
{
	if (number == 0) return{};
	vector<int> res;

	int tmp = number;
	while (tmp != 0)
	{
		res.push_back(tmp % 10);
		tmp /= 10;
	}
	return res;
}

int main()
{
	int numCases;
	cin >> numCases;

	unordered_map<int, int> umap;
	for (int i = 0; i <= 9; i++)
		umap[i] = i;

	for (int i = 0; i<numCases; i++)
	{
		int N;
		cin >> N;

		if (N == 0)
		{
			cout << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
			continue;
		}

		unordered_map<int, int> tmp = umap;
		int last = 0;
		int j = 1;
		while (tmp.size() != 0)
		{
			int dealt = N*j;
			vector<int> digits = digitsContained(dealt);
			for (auto d : digits)
			if (tmp.find(d) != tmp.end())
				tmp.erase(d);
			j++;
		}
		cout << "Case #" << i + 1 << ": " << (j - 1)*N << endl;
	}

	return 0;
}