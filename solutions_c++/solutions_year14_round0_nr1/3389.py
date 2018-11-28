#include <iostream>
using namespace std;

int main(){
	int T, x, firstMap[5][5], secondMap[5][5], ans1, ans2, possible[5], ans;
	cin >> T;

	for (int i1 = 0; i1 < T; i1++){
		cin >> ans1;
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++){
				cin >> firstMap[i][j];
			}
			if (i == ans1 - 1){
				for (int j = 0; j < 4; j++){
					possible[j] = firstMap[i][j];
				}
			}
		}
		cin >> ans2;
		int multi = 0;
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++){
				cin >> secondMap[i][j];
			}
			if (i == ans2 - 1){
				for (int j = 0; j < 4; j++){
					for (int k = 0; k < 4; k++){
						if (possible[k] == secondMap[i][j]){
							ans = possible[k];
							multi++;
						}
					}
				}
			}
		}
		cout << "Case #" << i1+1 << ": ";
		if (multi == 1){cout << ans << endl;}
		else if (multi > 1){cout << "Bad magician!" << endl;}
		else if (multi == 0){cout << "Volunteer cheated!" << endl;}
	}
	cin >> T;
	return 0;
}