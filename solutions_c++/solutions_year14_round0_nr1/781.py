#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <iostream>
using namespace std;

int arr1[4][4], arr2[4][4];
int r1, r2;

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("Aoutput.txt", "w", stdout);

	int T;
	cin >> T;
	for(int tt = 1; tt <= T; ++tt)
	{
		cin >> r1;
		for(int i = 0; i < 4; ++i)
			for(int j = 0; j < 4; ++j)
				cin >> arr1[i][j];
		cin >> r2;
		for(int i = 0; i < 4; ++i)
			for(int j = 0; j < 4; ++j)
				cin >> arr2[i][j];
		--r1, --r2;

		int q = 0;
		for(int i = 0; i < 4; ++i)
			for(int j = 0; j < 4; ++j)
				if(arr1[r1][i] == arr2[r2][j])
					++q;
		if(q == 0)
			cout << "Case #" << tt << ": Volunteer cheated!\n";
		else if(q > 1)
			cout << "Case #" << tt << ": Bad magician!\n";
		else
		{
			for(int i = 0; i < 4; ++i)
				for(int j = 0; j < 4; ++j)
					if(arr1[r1][i] == arr2[r2][j])
						cout << "Case #" << tt << ": " << arr1[r1][i] << endl;
		}
	}
	
	return 0;
}