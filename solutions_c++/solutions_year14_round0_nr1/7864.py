#include <iostream>
#include <fstream>

using namespace std;

void main(){

	const short int n = 4;
	
	short int T = 0;

	ifstream input("A-small-attempt0.in");
	ofstream output("output.txt");

	input>>T;

	for(short int i = 0; i < T; i++){

		short int r1,r2;

		input>>r1;
		r1--;

		short int** cards1 = new short int* [n];
		for(short int j = 0; j < n; j++){
			cards1[j] = new short int [n];
		};

		for(short int j = 0; j < n; j++){
			for(short int k = 0; k < n; k++){
				input>>cards1[j][k];
			}
		};

		input>>r2;
		r2--;

		short int** cards2 = new short int* [n];
		for(short int j = 0; j < n; j++){
			cards2[j] = new short int [n];
		};

		for(short int j = 0; j < n; j++){
			for(short int k = 0; k < n; k++){
				input>>cards2[j][k];
			}
		}

		short int card = 0, amount = 0;

		for(short int j = 0; j < n; j++){
			for(short int k = 0; k < n; k++){
				if(cards1[r1][j] == cards2[r2][k]){
					card = cards1[r1][j];
					amount++;
				};
			};
		};

		if(amount == 0) { 
			output<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
		} else {
			if(amount == 1) { 
				output<<"Case #"<<i+1<<": "<<card<<endl;
			} else {
				{ 
					output<<"Case #"<<i+1<<": Bad magician!"<<endl;
				}
			};
		};
	};
	system("pause");
}