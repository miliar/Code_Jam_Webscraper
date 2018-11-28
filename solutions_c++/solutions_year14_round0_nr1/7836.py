#include <iostream>

using namespace std;

int main(){
	bool cards[16];
	bool array[4][4];


	int nCases;
	cin >> nCases;

	int row, a[4];

	for(int i=0; i<nCases; i++){
		for(int j=0; j<16;j++)
			cards[j] = false;
		int nSol = 0;
		int sol;
		cin >> row;
		for(int j=0; j<4; j++){
			cin >> a[0] >> a[1] >> a[2] >> a[3];
			if(j == row-1){
				for(int k=0; k<4; k++)
					cards[a[k]-1] = true;
			}	
		}

		cin >> row;
		for(int j=0; j<4; j++){
			cin >> a[0] >> a[1] >> a[2] >> a[3];
			if(j == row-1){
				for(int k=0; k<4; k++){
					if(cards[a[k]-1]){
						nSol++;
						sol = a[k];
					}
				}
			}	
		}
		cout << "Case #" << i+1 << ": ";
		if(nSol == 1)
			 cout << sol << endl;
		else if(nSol == 0)
			cout << "Volunteer cheated!" << endl;
		else
			cout << "Bad magician!" << endl;

	}

	return 0;
}
