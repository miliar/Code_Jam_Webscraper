#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
using namespace std;

int cards[4][4];
int chosen[17];

int main() {
	int T, row, cnt, card;
	cin >> T;
	for (int t=1; t<=T; t++) {
		memset(chosen, 0, sizeof(chosen));
		for (int i=0; i<2; i++) {
			cin >> row;
			--row;
			for (int r=0; r<4; r++) {
				for (int c=0; c<4; c++) {
					cin >> cards[r][c];
				}
			}
			for (int c=0; c<4; c++) {
				++chosen[ cards[row][c] ];
			}
		}

		cnt = 0;
		for (int i=1; i<=16; i++) {
			if (chosen[i]==2) {
				++cnt;
				card = i;
			}
		}
		
		printf("Case #%d: ", t);
		if (cnt==0)
			puts("Volunteer cheated!");
		else if (cnt==1)
			cout << card << endl;
		else
			puts("Bad magician!");
	}
}
