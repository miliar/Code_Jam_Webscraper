#include <iostream>
using namespace std;
#include<vector>
#include<iomanip>
#include <stdio.h>
int main() {
	freopen("output.txt", "w", stdout);
	int test, count = 1;
	char arr[4][4];
	cin >> test;
	while (count <= test) {
		int counter3, counter4, counter1 = 0, counter2 = 0, count_dot = 0;
		char check3, check4;





		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				cin >> arr[i][j];
				if (arr[i][j] == '.')
					count_dot++;
			}
		}




		char check1 = arr[0][0], check2 = arr[0][3];
		for (int i = 0; i < 4; i++) {




			if ((arr[i][i] == check1 || arr[i][i] == 'T') && check1!='.') {
				if (check1 == 'T' )
					check1 = arr[1][1];
				counter1++;
			}




			if ((arr[i][3 - i] == check2 || arr[i][3 - i] == 'T') && check2!='.') {
				if (check2 == 'T')
					check2 = arr[1][2];
				counter2++;
			}




			counter3 = 0;
			check3 = arr[i][0];
			for (int j = 0; j < 4; j++) {
				if (check3 == '.')
					break;
				if (check3 == 'T')
					check3 = arr[i][j + 1];
				if (arr[i][j] == check3 || arr[i][j] == 'T' )
					counter3++;
				else
					break;
			}
			if (counter3 == 4)
				break;








			counter4 = 0;
			check4 = arr[0][i];
			for (int j = 0; j < 4; j++) {
				if (check4 == '.')
					break;
				if (check4 == 'T')
					check4 = arr[j + 1][i];
				if (arr[j][i] == check4 || arr[j][i] == 'T' )
					counter4++;
				else
					break;
			}
			if (counter4 == 4)
				break;
		}
		if (counter1 == 4)
			cout << "Case #" << count << ": " << check1 << " won\n";
		else if (counter2 == 4)
			cout << "Case #" << count << ": " << check2 << " won\n";
		else if (counter3 == 4)
			cout << "Case #" << count << ": " << check3 << " won\n";
		else if (counter4 == 4)
			cout << "Case #" << count << ": " << check4 << " won\n";
		else if (count_dot > 0)
			cout << "Case #" << count << ": Game has not completed\n";
		else if (count_dot == 0)
			cout << "Case #" << count << ": Draw\n";
		count++;
	}
}
