#include <iostream>
using namespace std;

int main(){
	int T; cin >> T;
	int ** table1 = new int*[4];
	int ** table2 = new int*[4];
	for(int i = 0; i < 4; i++){
		table1[i] = new int[4];
		table2[i] = new int[4];
	}
	for(int t = 1; t <= T; t++){
		int ans1, ans2;
		cin >> ans1;
		ans1--;
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				cin >> table1[i][j];
			}
		}
		cin >> ans2;
		ans2--;
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				cin >> table2[i][j];
			}
		}

		int res = -1;
		int count = 0;
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				if(table1[ans1][i] == table2[ans2][j]){
					res = table1[ans1][i];
					count++;
				}
			}
		}
		if(count > 1)
			cout << "Case #" << t << ": " << "Bad magician!" << endl;
		else if(res == -1)
			cout << "Case #" << t << ": " << "Volunteer cheated!" << endl;
		else
			cout << "Case #" << t << ": " << res << endl;
	}

	return 0;
}
