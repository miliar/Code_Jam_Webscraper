#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
	int cases;
	cin >> cases;
	for(int i = 0;i < cases; i++)
	{
		vector<vector<int>> map1;
		vector<vector<int>> map2;
		int a1, a2;
		cin >> a1;
		for(int k = 0; k < 4; k++)
		{
			vector<int> temp;
			for(int j = 0; j < 4; j++)
			{
				int t;
				cin >> t;
				temp.push_back(t);
			}
			map1.push_back(temp);
		}
		cin >> a2;
		for(int k = 0; k < 4; k++)
		{
			vector<int> temp;
			for(int j = 0; j < 4; j++)
			{
				int t;
				cin >> t;
				temp.push_back(t);
			}
			map2.push_back(temp);
		}
		vector<int> possibilities;
		for(int j = 0; j < 4; j++)
		{
			possibilities.push_back(map1[a1-1][j]);
			//std::cout << "Push: " << map1[a1-1][j] << endl;
		}
		int results = 0;
		int result = -1;
		for(int j = 0; j < 4; j++)
		{
			for(int k = 0; k < possibilities.size(); k++)
			{
				if(possibilities[k] == map2[a2-1][j] && possibilities[k] != -1)
				{
					results++;
					result = possibilities[k];
				}
			}
		}

		// int results = 0;
		// int result = -1;
		// for(int j = 0; j < possibilities.size(); j++)
		// {
		// 	if(possibilities[j] != -1)
		// 	{
		// 		results++;
		// 		result = possibilities[j];
		// 	}
		// }
		//std::cout << "Results: " << results << " Result: " << result << endl;
		if(results == 0)
		{
			cout << "Case #" << i+1 << ": " << "Volunteer cheated!" << endl;
		}
		else if(results == 1)
		{
			cout << "Case #" << i+1 << ": " << result << endl;
		}
		else
		{
			cout << "Case #" << i+1 << ": " << "Bad magician!" << endl;
		}
	}
	return 0;
}