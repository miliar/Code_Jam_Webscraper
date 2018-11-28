#include <iostream>
#include <cstring>
using namespace std;

void main(){
	
	freopen("op.txt", "w", stdout);

	int T,
		s[2],
		Grid[2][4][4],
		Map[17],
		card;

	cin >> T;

	for(int t=1 ; t<=T ; t++){
		card = -1;
		memset(Map, 0, 17*sizeof(int));

		for(int idx=2 ; idx-- ; ){
			cin >> s[idx];
			for(int i=0 ; i<4 ; i++) for(int j=0 ; j<4 ; j++) cin >> Grid[idx][i][j];

			for(int i=4 ; i-- ; ) Map[Grid[idx][s[idx]-1][i]]++;
		}

		for(int i=1 ; i<17 ; i++)
			if(Map[i] == 2)
				if(card == -1)
					card = i;
				else
					card = -2;

		cout << "Case #" << t << ": ";
		if(card == -1)
			cout << "Volunteer cheated!\n";
		else if(card == -2)
			cout << "Bad magician!\n";
		else cout << card << endl;
	}

}