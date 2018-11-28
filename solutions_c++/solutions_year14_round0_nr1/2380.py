#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

using namespace std;

const string NONE = "Volunteer cheated!";
const string MULTI = "Bad magician!";

vector<vector<int> > arr1, arr2;
int sol1, sol2;

string solve();

int main()
{
	ifstream cin("MagicTrick.in");
	ofstream cout("MagicTrick.txt");

	int T;
	cin >> T;
	for(int t = 0; t < T; t++)
	{
		int temp;
			arr1.clear();
			arr2.clear();
			cin >> sol1;
			for(int i = 0; i < 4; i++)
			{
				vector<int> row;
				for(int j = 0; j < 4; j++)
				{
					cin >> temp;
					row.push_back(temp);
				}
				arr1.push_back(row);
			}
			cin >> sol2;
			for(int i = 0; i < 4; i++)
			{
				vector<int> row;
				for(int j = 0; j < 4; j++)
				{
					cin >> temp;
					row.push_back(temp);
				}
				arr2.push_back(row);
			}

		cout << "Case #" << t + 1 << ": " << solve() << endl;
	}

	return 0;
}

string solve()
{
	int id = -1, count = 0;
	for(int i = 0; i < 4; i++)
	{
		for(int j = 0; j < 4; j++)
		{
			if(arr1[sol1 - 1][i] == arr2[sol2 - 1][j])
			{
				count++;
				id = arr1[sol1 - 1][i];
			}
		}
	}

	if(count == 0) return NONE;
	else if(count > 1) return MULTI;

	stringstream ss;
	ss << id;
	return ss.str();
}
