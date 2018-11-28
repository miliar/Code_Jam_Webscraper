#include <iostream>

using namespace std;

const int N = 16;

void clear_R(int R[]) {

	for (int i =1; i <= N; i++) R[i] = 0;
	
}


int main () {

	int T;

	cin >> T;

	for (int i = 1; i <= T; i++) {
		
		int r1;
		cin >> r1;
		
		int R[N+1];
		clear_R(R);
		for (int i = 1; i <= 4; ++i)
			for (int j = 1; j <= 4; ++j) {
				int t; cin >> t;
				if (i == r1) 
					R[t]++;
			}

		int r2;
		cin >> r2;
		for (int i = 1; i <= 4; ++i)
			for (int j = 1; j <= 4; ++j) {
				int t; cin >> t;
				if (i == r2) 
					R[t]++;
			}

		cout << "Case #"<< i << ": ";
		
		int f = 0;
		int l = 0;
		for (int p = 1; p <= N; p++)
			if (R[p] == 2) f++, l = p;

		if ( f == 1 ) cout << l << endl;
		else if ( f == 0 ) cout << "Volunteer cheated!" << endl;
		else cout << "Bad magician!" << endl;		
	}


}