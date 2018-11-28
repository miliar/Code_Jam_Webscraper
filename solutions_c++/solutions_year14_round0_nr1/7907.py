/* Solution to CodeJam Problem A
@file PA-MagicTrick.c++
@author Kaleb Goering
@date April 11, 2014 */

#include <iostream>
#include <string>

using namespace std;

int compare(int* arr, int* narr) {
	int index = -1;
	int count = 0;

	for(int i = 0; i < 4; i++) {
		for(int j = 0; j < 4; j++) {
			if(arr[i] == narr[j]) {
				index = i;
				count++;
			}
		}
	}

	if(count < 1)
		return (-2);
	else if (count > 1)
		return (-1);
	else
		return arr[index];
	
			
}

int main() {
	int T = 0;
	cin >> T;
	
	int nums1[4][4];
	int nums2[4][4];

	for(int i = 1; i <= T; i++) {
		int row1, row2;
		cin >> row1;
		for(int j = 0; j < 4; j++){
			for(int k = 0; k < 4; k++) {
				cin >> nums1[j][k];
			}
			
		}

		cin >> row2;
		for(int j = 0; j < 4; j++){
			for(int k = 0; k < 4; k++) {
				cin >> nums2[j][k];
			}
			
		}


		int ans = compare(nums1[row1 - 1], nums2[row2 -1]);
		if(ans > 0)
			cout << "Case #" << i << ": " << ans << endl;
		else if(ans < (-1))
			cout << "Case #" << i << ": Volunteer cheated!" << endl;
		else
			cout << "Case #" << i << ": Bad magician!" << endl;
	}
	return 0;
}
