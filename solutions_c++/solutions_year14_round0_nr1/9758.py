#include<iostream>
#include<cstdio>
#include<math.h>
#include<algorithm>
#include<vector>
using namespace std;
int main(){
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t = 0;
	cin >> t;
	int c = 0;
	while (t--){
		int first, second;
		cin >> first;
		int arr[4][4];
		int row1[4], row2[4];
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++){
				cin >> arr[i][j];
				if (i == first-1){
					row1[j] = arr[i][j];
				}
			}
		cin >> second;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++){
				cin >> arr[i][j];
				if (i == second-1){
					row2[j] = arr[i][j];
				}
			}

		int count = 0;
		int ans = 0;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++){
				if (row1[i] == row2[j]){
					count++;
					ans = row1[i];
				}
			}
		if (count == 1){
			cout << "Case #" << ++c << ": " << ans << endl;
		}else if (count>1){
			cout << "Case #" << ++c << ": Bad magician!" << endl;
		}
		else if (count == 0){
			cout << "Case #" << ++c << ": Volunteer cheated!" << endl;
		}
	}
	return 0;
}