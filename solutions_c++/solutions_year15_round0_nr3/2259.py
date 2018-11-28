#include <iostream>
using namespace std;

int result[4][4] = { 1, 2, 3, 4,
					2, -1, 4, -3,
					3, -4, -1, 2,
					4, 3, -2, -1 };

// i : 2, j : 3, k : 4
int transfer(int a, int b){
	if (a < 0){
		if (b < 0){
			return (result[(-(a)-1)][(-(b)-1)]);
		}
		else{
			return -(result[(-(a)-1)][b - 1]);
		}
	}
	else if (b < 0){
		return -(result[a - 1][-(b)-1]);
	}
	return (result[a - 1][b - 1]);
}


int main(){
	int T;
	int L, X; // L characters duplicate X times
	int space[100000];
	int spare[100000];
	int size;
	int indexEnd, indexStart;
	int value;
	char input;

	int flagI, flagJ, flagK;

	cin >> T;

	for (int i = 1; i <= T; i++){
		flagI = 0; flagJ = 0; flagK = 0;
		indexEnd = 0; indexStart = 0;
		value = 1;
		size = 0;
		cin >> L >> X;   // L * X  10^16 юлго
		for (int j = 0; j < L; j++){
			cin >> input;
			if (input == 'i')
				spare[j] = 2;
			else if (input == 'j')
				spare[j] = 3;
			else if (input == 'k')
				spare[j] = 4;
		}


		

		while (1){
			
			for (int j = 0; j < L; j++){
				space[j] = spare[j];
			}
			X--;

			for (int j = 0; j < L; j++){
				value = transfer(value, space[j]);
				//cout << value;
				if (flagI == 0){
					if (value == 2){
						flagI = 1;
						value = 1;
					//	cout << " I set " << endl;
					}
				}
				else if (flagJ == 0){
					if (value == 3){
						flagJ = 1;
						value = 1;
					//	cout << " J set " << endl;
					}
				}
				else if (flagK == 0){
					if (value == 4){
						flagK = 1;
					//	cout << " K set " << endl;
					}
				//	else cout << " K unseted and pass " << endl;
				}
				else{
					if (value != 4){
						flagK = 0;
				//		cout << " K unset " << endl;
					}
				//	else cout << " K seted and pass " << endl;
				}
			}
			if (X == 0) break;  // flag all set or unset 
		}
		//cout << endl;
		cout << "Case #" << i << ": ";
		if (flagI == 1 && flagJ == 1 && flagK == 1) cout << "YES" << endl;
		else cout << "NO" << endl;

	}

	return 0;
}