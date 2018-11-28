#include <iostream>

using namespace std;

int main(){
	int T; cin >> T;
	for (int test = 1; test <= T; test++){
		int num_match = 0;
		int row1, row2; 
		int first[4], second[4];
		cin >> row1;
		for (int i = 1; i <= 4; i++){
			int a, b, c, d; cin >> a >> b >> c >> d;
			if (row1 == i){
				first[0] = a; first[1] = b; first[2] = c; first[3] = d;
			}
		}
		cin >> row2;
		for (int i = 1; i <= 4; i++){
			int a, b, c, d; cin >> a >> b >> c >> d;
			if (row2 == i){
				second[0] = a; second[1] = b; second[2] = c; second[3] = d;
			}
		}
		int found = -1;
		for (int i = 0; i < 4; i++){
			for (int j = 0 ; j < 4; j++){
				if (first[i] == second[j]) {num_match++; found = first[i];}
			}

		}
		cout << "Case #" << test << ": ";
		if (num_match == 1){
			cout << found;
		} else if (num_match > 1){
			cout << "Bad magician!";
		} else cout << "Volunteer cheated!";
		cout << endl;
	}

	return 0;
}