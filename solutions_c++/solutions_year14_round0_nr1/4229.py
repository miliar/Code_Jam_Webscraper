#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int main() {
	if(fopen("magic.in","r")) {
		freopen("magic.in","r",stdin);
		freopen("magic.out","w",stdout);
	}
	int arr[5][5], newarr[5][5], ansnum, ans;
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++) {
		int a1, a2;
		ansnum = 0;
		cin >> a1;
		for(int j = 1; j <= 4; j++) {
			for(int k = 1; k <= 4; k++) {
				cin >> arr[j][k];
			}
		}
		cin >> a2;
		for(int j = 1; j <= 4; j++) {
			for(int k = 1; k <= 4; k++){
				cin >> newarr[j][k];
			}
		}
		cout << "Case #";
		cout << i; 
		cout << ": ";

		for(int j = 1; j <= 4; j++) {
			for(int k = 1; k <= 4; k++) {
				if(arr[a1][j] == newarr[a2][k]) {
					ansnum++;
					ans = arr[a1][j];
				}
			}
		}
		if(ansnum == 0) {
			cout << "Volunteer cheated!" << '\n';
		}
		if(ansnum == 1) {
			cout << ans << '\n';
		}
		if(ansnum > 1) {
			cout << "Bad magician!" << '\n';
		}
	}
	return 0;
}