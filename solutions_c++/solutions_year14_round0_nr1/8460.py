#include <iostream>

using namespace std;

void cards(int t){	
	cout << "Case #" << t << ": ";
	int choice;
	int cards[4][4];

	cin >> choice;
	for(int i(0); i<4; i++)
		for(int j(0); j<4; j++)
			cin >> cards[i][j];
	
	int pos[4];
	for(int j(0); j<4; j++)
		pos[j] = cards[choice-1][j];

	cin >> choice;
	for(int i(0); i<4; i++)
		for(int j(0); j<4; j++)
			cin >> cards[i][j];

	bool done(false);
	int card;
	for(int i(0); i<4; i++){
		for(int j(0); j<4; j++){
			if(cards[choice-1][j] == pos[i]){
				card = pos[i];
				if(done){
					cout << "Bad magician!" << endl;
					return;
				}
				done = true;
			}
		}
	}
	
	if(done)
		cout << card << endl;
	else
		cout << "Volunteer cheated!" << endl;
}

int main(){
	int T;
	cin >> T;
	for(int t(0); t<T; t++){
		cards(t+1);
	}
	return 0;
}
