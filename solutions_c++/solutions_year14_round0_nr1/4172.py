#include<iostream>
#include<set>
#include<vector>
#include<algorithm>
#include<cstdio>
using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	int count = 0;
	while (T--)
	{
		if (count != 0)
			cout << endl;
		count++;
		int guess1,guess2;
		cin >> guess1;
		guess1--;
		vector<int> row1,row2;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				int temp;
				cin >> temp;
				if (i == guess1)
					row1.push_back(temp);
			}
		}
		cin >> guess2;
		guess2--;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				int temp;
				cin >> temp;
				if (i == guess2)
					row2.push_back(temp);
			}
		}
		//Find Intersection between two vectors
		vector<int>result;
		for (int i = 0; i < row1.size(); i++)
		{
			for (int j = 0; j < row1.size(); j++)
			{
				if (row1[i] == row2[j])
				{
					result.push_back(row2[j]);
					break;
				}
				
			}
		}
		cout << "Case #"<<count<<": ";
		if (result.size() == 1)
			cout << result[0] ;
		else if (result.size() == 0)
			cout << "Volunteer cheated!";
		else
			cout << "Bad magician!" ;

	}
	return 0; 
}