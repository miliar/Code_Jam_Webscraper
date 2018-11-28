#include <iostream>

using namespace std;

int main()
{
	int tc;	// number of test cases
	int ans[2];	// both answers
	int arr[2][4][4];	// both arrangements
	int result;	// the result
	int i, j, k;	// counters for loops

	cin >> tc;

	for(i = 0; i < tc; i++)
	{
		cin >> ans[0];
		for(j = 0; j < 4; j++)
			for(k = 0; k < 4; k++)
				cin >> arr[0][j][k];
		cin >> ans[1];
		for(j = 0; j < 4; j++)
			for(k = 0; k < 4; k++)
				cin >> arr[1][j][k];
		ans[0]--;
		ans[1]--;
		result = 0;

		for(j = 0; j < 4; j++)
			for(k = 0; k < 4; k++)
				if(arr[0][ans[0]][j] == arr[1][ans[1]][k])
				{
					if(result == 0)
						result = arr[0][ans[0]][j];
					else
						result = 17;
				}

		cout << "Case #" << (i+1) << ": ";
		switch(result)
		{
			case 0:
				cout << "Volunteer cheated!";
				break;
			case 17:
				cout << "Bad magician!";
				break;
			default:
				cout << result;
		}
		cout << endl;
	}
	return 0;
}
