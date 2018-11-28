#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <stdio.h>

using namespace std;
int main()
{
	FILE *out;
	FILE *in;

	freopen_s(&in,"A-small-attempt1.in", "r", stdin);
	freopen_s(&out,"A-small-attempt1.out", "w", stdout);

	int T;
	cin >> T;

	for (int i = 1; i <= T; i++)
	{
		int array1[4][4];
		int array2[4][4];

		int answer1;
		int answer2;

		cin >> answer1;
		for (int r = 0; r < 4; r++){
			for (int c = 0; c < 4; c++){
				cin >> array1[r][c];
			}
		}

		cin >> answer2;
		for (int r = 0; r < 4; r++){
			for (int c = 0; c < 4; c++){
				cin >> array2[r][c];
			}
		}

		int result = -1;
		bool bBadMagician = false;

		for (int j = 0; j < 4 && !bBadMagician; j++){
			for (int k = 0; k < 4; k++){
				if (array1[answer1-1][j] == array2[answer2-1][k]){
					
					if (result == -1) result = array1[answer1-1][j]; 
					else bBadMagician = true;
					break;
				}
			}
		}

		cout << "Case #" << i << ": ";

		//Case #1: 7
		//Case #2: Bad magician!
		//Case #3: Volunteer cheated!

		if (bBadMagician) cout << "Bad magician!";
		else if (result == -1) cout << "Volunteer cheated!";
		else cout << result;
		
		cout << endl;

	}

	//system("pause");
}