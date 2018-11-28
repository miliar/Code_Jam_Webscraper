#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iterator>
#include <fstream>
#include <sstream>
#include <istream>
#include <unordered_map>
#include <map>

using namespace std;

int main()
{
	int numCases;
	cin >> numCases;

	for (int i = 0; i<numCases; i++)
	{
		int N;
		cin >> N; // number of elements in each row or col

		int num_cin = N*(2 * N - 1);
		unordered_map<int, int> count;
		int tmp;
		int j = 0;

		while (j < num_cin)
		{
			cin >> tmp;
			if (count.find(tmp) == count.end())
				count[tmp] = 1;
			else
				count[tmp]++;

			j++;
		}
		vector<int> res;
		for (unordered_map<int, int>::iterator it = count.begin(); it != count.end(); it++){
			if (it->second % 2)
				res.push_back(it->first);
		}

		sort(res.begin(), res.end());
		cout << "Case #" << i + 1 << ": ";
		for (int i = 0; i < res.size() - 1; i++)
			cout << res[i] << " ";
		cout << res[res.size() - 1] << endl;
	}

	return 0;
}