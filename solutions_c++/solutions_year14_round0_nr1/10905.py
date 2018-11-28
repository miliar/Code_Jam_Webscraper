#include <iostream>
#include <set>
#include <algorithm>
#include <vector>
using namespace std;


int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		int ans1, ans2;
		int arr1[4][4];
		int arr2[4][4];

		cin >> ans1;
		ans1--;

		for (int j = 0; j < 4; ++j)
		{
			for (int k = 0; k < 4; ++k)
			{
				cin >> arr1[j][k];
				//cout << arr1[j][k] << " ";
			}
			//cout << endl;
		}

		cin >> ans2;
		ans2--;

		for (int j = 0; j < 4; ++j)
		{
			for (int k = 0; k < 4; ++k)
			{
				cin >> arr2[j][k];
				//cout << arr2[j][k] << " ";
			}
			//cout << endl;
		}

		int count = 0;
		int answer;
		for (int j = 0; j < 4; ++j)
		{
			for (int k = 0; k < 4; ++k)
			{
				if ( arr1[ans1][j] == arr2[ans2][k] )
				{	
					count++;
					answer = arr1[ans1][j];
				}
			}
		}

		cout << "Case #" << i + 1 << ": ";

		if ( count == 0 )
		{
			cout << "Volunteer cheated!" << endl;
		} else if ( count == 1 )
		{
			cout << answer << endl;
		} else {
			cout << "Bad magician!" << endl;
		}
	}
	return 0;
}