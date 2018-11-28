#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	freopen("A-small-attempt0.in","r", stdin);
	freopen("out.txt","w",stdout);
	
	int N;
	cin >> N;
	for(int n=1; n<=N; n++) {
		int row1, row2;
		int card1[4][4], card2[4][4];
		cin >> row1;
		for(int i=0; i<4; i++) for(int j=0; j<4; j++) cin >> card1[i][j];
		cin >> row2;
		for(int i=0; i<4; i++) for(int j=0; j<4; j++) cin >> card2[i][j];
		row1--;
		row2--;
		
		//solution
		int tot=0, ans;
		for(int i=0; i<4; i++) for(int j=0; j<4; j++) if(card1[row1][i] == card2[row2][j]) tot++, ans=card1[row1][i];
		
		cout << "Case #" << n << ": ";
		if(tot==1) cout << ans << endl;
		else if(tot>1) cout << "Bad magician!" << endl;
		else cout << "Volunteer cheated!" << endl;
	}
}
