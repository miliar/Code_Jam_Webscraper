#include <iostream>
using namespace std;

int row[16];

void getHand() {
	int a, b, c, d, sel;
	cin >> sel;
	for (int i=1 ; i<=4 ; i++) {
		cin >> a >> b >> c >> d;
		if (i!=sel) continue;
		row[a-1]++;
		row[b-1]++;
		row[c-1]++;
		row[d-1]++;
	}
}

int main() {
	int T;
	cin >> T;
	for (int t=1 ; t<=T ; t++) {
		for (int i=0 ; i<16 ; i++)
			row[i] = 0;
		getHand();
		getHand();
		int found = 0, is;
		for (int i=0 ; i<16 ; i++)
			if (row[i]==2) {
				found++;
				is = i+1;
			}
		
		cout << "Case #" << t << ": ";
		if (found==1) cout << is << endl;
		else if (found>1) cout << "Bad magician!" << endl;
		else cout << "Volunteer cheated!" << endl;
	}
	return 0;
}