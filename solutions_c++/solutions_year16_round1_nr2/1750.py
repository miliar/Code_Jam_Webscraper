#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

int main()
{
	int inputs;
	int size;
	int in;

	vector<int> row;

	vector<int> odd;

	unordered_map<int, int> count;

	cin >> inputs;

	for(int i = 0; i < inputs; i++)
	{
		cin >> size;

		// Get all inputs
		for(int j = 0; j < (size *2)- 1; j++)
		{
			for(int k = 0; k < size; k++)
			{
				cin >> in;

				row.push_back(in);
			}
		}

		for(int j = 0; j < row.size(); j++)
		{
			count[row[j]]++;
		}

		for(int j = 0; j < row.size(); j++)
		{
			if(count[row[j]] % 2 == 1)
			{
				odd.push_back(row[j]);
			}
		}

		sort(odd.begin(), odd.end());
		odd.erase( unique( odd.begin(), odd.end() ), odd.end() );

		cout << "Case #" << i + 1 << ": ";

		for(int j = 0; j < odd.size(); j++)
		{
			cout << odd[j];
			if(j != odd.size() - 1)
			{
				cout << " ";
			}
		}
		cout << endl;

		row.clear();
		odd.clear();
		count.clear();
	}

	return 0;
}