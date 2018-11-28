#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;

int T;
int ar[2][4][4];
int r[2];

void solve() {
	int cnt = 0;
	int pos = -1;
	for(int i=0; i < 4; i++) {
		for(int j=0; j<4; j++) {
			if(ar[0][r[0]][i] == ar[1][r[1]][j]) {
				pos = i;
				cnt++;
			}
		}
	}

	if(!cnt) {
		cout << "Volunteer cheated!" << endl;
	} else if(cnt == 1) {
		cout << ar[0][r[0]][pos] << endl;
	} else {
		cout << "Bad magician!" << endl;
	}
}


int main() {
	cin >> T;
	for(int l=1; l<=T; l++) {
		cout << "Case #" << l << ": ";
		for(int i=0; i<2; i++) {
			cin >> r[i];
			r[i]--;
			for(int j=0; j<4; j++) {
				for(int k=0; k<4; k++) {
					cin >> ar[i][j][k];
				}
			}
		}
		solve();
	}
	return 0;
}