#include <iostream>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <utility>

using namespace std;

int main()
{
	int T ;
	cin >> T;
	for ( int test = 1 ; test <= T ; test++ )
	{
		int n = 0;
		int solve = 0;
		bool solveExist = true;
		cin >> n;

		vector<string> words;
		words.resize(n);
		for ( int i = 0 ; i < n ; ++i )
		{
			cin >> words[i];
		}

		vector<int> position;
		position.resize(n);
		for ( int j = 0 ; j < n ; ++j )
			position[j] = 0;

		while ( position[0] < words[0].size() )
		{
			vector<int> values(0);
			char symbol = words[0][position[0]];
			for ( int p = 0 ; p < n ; ++p )
			{
				int counter = 0;
				while ( position[p] < words[p].size() )
				{
					if ( words[p][position[p]] == symbol )
					{
						counter++;
					}
					else {
							break;
						 }
					position[p]++;
				}
				if ( counter == 0 )
				{
					solveExist = false;
					break;
				}
				values.push_back(counter);
			}
			if (!solveExist) break;

			sort(values.begin(), values.end());
			int value = values[(n-1)/2];
			for ( int p = 0 ; p < n ; ++p )
			{
				solve += abs(values[p]-value);
			}
		}

		for ( int j = 0 ; j < n ; ++j )
			if ( position[j] < words[j].size() )
			{
				solveExist = false;
				break;
			}

		cout << "Case #" << test << ": ";
		if (solveExist)
		{
			cout << solve;
		}
		else {
				cout << "Fegla Won";
			 }
		cout << endl;
	}
}
