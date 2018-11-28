#include <iostream>

using namespace std;
int main(int argc, char ** argv) 
{
	int T;
	

	cin >> T;
	for(int tIndex = 0; tIndex < T; tIndex++) {
		int a;
		int vals[2][4];
		for(int boardNo = 0; boardNo < 2; boardNo++) {
			cin >> a;
			for(int j = 1; j <= 4; j++) {
				if(a == j) {// read this line
					for(int k = 0; k < 4; k++) {
						cin >> vals[boardNo][k];
					}
				} else {
					for(int k = 0; k < 4; k++) {
						int tmp;
						cin >> tmp;
					}
				}
			}
		}

		// find the common numbers in the 2 vals
		int state = 0; // cheat
		int common_ans = -1;
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				if(vals[0][i] == vals[1][j]) {
					if(common_ans < 0) {
						common_ans = vals[0][i];
						state = 1; // ok
					}
					else {
						state = 2; // bad magician
					}

				}
			}
		}
		cout << "Case #" << (tIndex + 1) << ": ";
		switch(state){
			case 0:
				cout << "Volunteer cheated!" << endl;
				break;
			case 1:
				cout << common_ans << endl;
				break;
			case 2:
				cout << "Bad magician!" << endl;
				break;
		}

		
	}
	return 0;
}