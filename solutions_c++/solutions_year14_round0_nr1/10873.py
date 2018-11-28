#include <iostream>


using namespace std;


#define WIDTH 4
#define HEIGHT 4


void startGame(int gameCounter){

	int input;
	cin >> input;

	int i,j;
	int rowChosen[WIDTH];

	for (i = 0; i < (input - 1) * 4; i++){
		cin >> j; 
	}
	for (j = 0; j < WIDTH; j++){
		cin >> rowChosen[j];
	}
	for (j = 0; j < (4 - input) * 4; j++){
		cin >> i;
	}

	cin >> input;
	int rowChosen2[WIDTH];


	for (i = 0; i < (input - 1) * WIDTH; i++){
		cin >> j; 
	}
	for (j = 0; j < WIDTH; j++){
		cin >> rowChosen2[j];
	}

	int counter = 0;
	int answer;

	for (i = 0; i < WIDTH; i++){
		for (j = 0; j < WIDTH; j++){
			if (rowChosen[i] == rowChosen2[j]){
				counter++;
				answer = rowChosen[i];
			}
		}
	}

	for (j = 0; j < (4 - input) * 4; j++){
		cin >> i;
	}

	switch(counter){
		case 0: cout << "Case #"<< gameCounter <<": Volunteer cheated!" << endl;
		break;
		case 1: cout << "Case #" << gameCounter <<": " << answer << endl;
		break;
		default:
		cout << "Case #" << gameCounter <<": Bad magician!" << endl;
	}
}

int main(){
	int inputCount;
	cin >> inputCount;
	int i;
	for (i = 0; i <inputCount; i++ ){
		startGame(i+1);
	}
	return 0;
}