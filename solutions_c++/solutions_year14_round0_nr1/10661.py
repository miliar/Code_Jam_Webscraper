#include <iostream>
#include <set>
#include <list>
using namespace std;

int main() {
	// your code goes here
	int cases, answer;
	set<int> holder;
	int arr[4][4];
	cin >> cases;
	
	int number = 0;
	for (int i = 0; i < cases; i++)
	{
		int count = 0;
		cin >> answer;
		for (int x = 0; x < 4; x++)
		{
			for (int y = 0; y < 4; y++)
			{
				cin >> arr[x][y];
			}
		}
		for (int j = 0; j < 4; j++)
		{
			holder.insert(arr[answer - 1][j]);
		}
		cin >> answer;
		for (int x = 0; x < 4; x++)
		{
			for (int y = 0; y < 4; y++)
			{
				cin >> arr[x][y];
			}
		}
		for (int j = 0; j < 4; j++)
		{
			if (holder.count(arr[answer - 1][j]) == 1)
			{
				count++;
				number = arr[answer - 1][j];
			}
		}
		holder.clear();
		if (count == 1)
			cout << "Case #" << i + 1 << ": " << number << endl;
		else if (count > 1)
			cout << "Case #" << i + 1 << ": " << "Bad magician!" << endl;
		else if (count == 0)
			cout << "Case #" << i + 1 << ": " << "Volunteer cheated!" << endl;
		count = 0;
	}
	

	return 0;
}

