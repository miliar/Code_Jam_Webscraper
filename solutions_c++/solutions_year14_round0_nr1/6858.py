#include <iostream>
#include <bitset>

using namespace std;

int main()
{
	int T;
	cin >> T;

	for (int i = 1; i <= T; ++i)
	{
		int first, second, arr1[4][4], arr2[4][4], result = -1;
		bitset<17> C;
		C.reset();

		cin >> first;
		--first;

		for (int j = 0; j < 4; ++j)
		{
			for (int k = 0; k < 4; ++k)
			{
				cin >> arr1[j][k];
			}
		}
		for (int j = 0; j < 4; ++j)
		{
			C.flip(arr1[first][j]);
		}

		cin >> second;
		--second;

		for (int j = 0; j < 4; ++j)
		{
			for (int k = 0; k < 4; ++k)
			{
				cin >> arr2[j][k];
			}
		}
		for (int j = 0; j < 4; ++j)
		{
			if(C[arr2[second][j]])
				result = arr2[second][j];
			C.flip(arr2[second][j]);
		}

		cout << "Case #"<<i<<": ";
		if(C.count() == 6)
			cout << result << "\n";
		else if(C.count() == 8)
			cout << "Volunteer cheated!\n";
		else
			cout << "Bad magician!\n";
	}
	return 0;
}