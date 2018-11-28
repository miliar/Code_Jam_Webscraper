#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	int t;
	cin >> t;
	int old_arr[4][4];
	int new_arr[4][4];
	for(int i = 0 ; i < t; ++i) {
		int r1;
		scanf("%d", &r1);
		for(int j = 0; j < 4; ++j) {
			scanf("%d %d %d %d", &old_arr[j][0], &old_arr[j][1], &old_arr[j][2], &old_arr[j][3]);
		}
		int r2;
		scanf("%d", &r2);
		for(int j = 0; j < 4; ++j) {
			scanf("%d %d %d %d", &new_arr[j][0], &new_arr[j][1], &new_arr[j][2], &new_arr[j][3]);
		}
		int counter = 0;
		int ans = 0;
		for(int j = 0; j < 4; ++j) {
			for(int k = 0; k < 4; ++k) {
				if(old_arr[r1-1][j] == new_arr[r2-1][k]) {
					counter++;
					ans = old_arr[r1-1][j];
				}
			}
		}
		cout << "Case #" << i+1 << ": ";
		if(counter == 1) {
			cout << ans << endl;
		} else if(counter == 0) {
			cout << "Volunteer cheated!" << endl;
		} else {
			cout << "Bad magician!" << endl;
		}
	}
	return 0;
}