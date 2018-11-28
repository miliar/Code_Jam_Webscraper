#include <iostream>
using namespace std;

int T, ans1, B1[5][5], ans2, B2[5][5];
int card;

void read(){
	int i, j;
	cin >> ans1;
	for (i = 1; i < 5; i++){
		for (j = 1; j < 5; j++){
			cin >> B1[i][j];
		}
	}
	cin >> ans2;
	for (i = 1; i < 5; i++){
		for (j = 1; j < 5; j++){
			cin >> B2[i][j];
		}
	}
}
void write(int i){
	switch (i){
	case 0:  
		cout << "Volunteer cheated!\n";
		break;
	case 1:
		cout << card << "\n";
		break;
	default:
		if (i > 1) cout << "Bad magician!\n";
	}
}
void solve(){
	int i, j, nrp = 0;
	read();

	for (i = 1; i < 5; i++){
		for (j = 1; j < 5; j++){
			if (B1[ans1][i] == B2[ans2][j]){
				nrp++;
				card = B2[ans2][j];
			}
		}
	}

	write(nrp);
}

int main(){
	int i;
	cin >> T;

	for (i = 1; i <= T; i++){
		cout << "Case #" << i << ": ";
		solve();
	}

	return 0;
}