#include <iostream>
#include <fstream>

using namespace std;

int main (int argc, char* argv[]) {

  if (argc < 2) {
    cout << "not enough arguments" << endl;
    return -1;
  }

  ifstream input(argv[1]); // open file 

  int numcases = 0;

  if (input.good()) {
    input >> numcases;

    for (int i = 1; i <= numcases; i++) {
		int rownum1 = 0;
		//grab 1st row number called
		input >> rownum1;
		
		//grab the rows
		int cards1[16];
		for (int j = 0; j < 16; j++) {
			input >> cards1[j];
		}
		
		//grab 2nd row number called
		int rownum2 = 0;
		input >> rownum2;
		
		//grab the rows again
		int cards2[16];
		for (int j = 0; j < 16; j++) {
			input >> cards2[j];
		}
		
		int answerrow[4]; //array for the row that contains the answer
		// fill answerrow with the numbers in that row.
		switch (rownum1) {
		case 1:
			for (int j = 0; j < 4; j++) {
				answerrow[j] = cards1[j];
			}
			break;
		case 2:
			for (int j = 0; j < 4; j++) {
				answerrow[j] = cards1[j+4];
			}
			break;
		case 3:
			for (int j = 0; j < 4; j++) {
				answerrow[j] = cards1[j+8];
			}
			break;
		case 4:
			for (int j = 0; j < 4; j++) {
				answerrow[j] = cards1[j+12];
			}
			break;
		default:
			cout << "Something went wrong for Case: " << i << endl;
			break;
		}
		
		
		//compare the 2nd row to the 1st row
		bool foundit = false; // can only be found once.
		bool badmage = false;// if found more than once, 'bad magician'.
		int answer = 0;
		switch (rownum2) {
		case 1:
			for (int j = 0; j < 4; j++) {
				for (int k = 0; k < 4; k++) {
					if(answerrow[j] == cards2[k]) {
						if(foundit)
							badmage = true;
						foundit = true;
						answer = cards2[k];
					}
				}
			}
			break;
		case 2:
			for (int j = 0; j < 4; j++) {
				for (int k = 0; k < 4; k++) {
					if(answerrow[j] == cards2[k+4]) {
						if(foundit)
							badmage = true;
						foundit = true;
						answer = cards2[k+4];
					}
				}
			}
			break;
		case 3:
			for (int j = 0; j < 4; j++) {
				for (int k = 0; k < 4; k++) {
					if(answerrow[j] == cards2[k+8]) {
						if(foundit)
							badmage = true;
						foundit = true;
						answer = cards2[k+8];
					}
				}
			}
			break;
		case 4:
			for (int j = 0; j < 4; j++) {
				for (int k = 0; k < 4; k++) {
					if(answerrow[j] == cards2[k+12]) {
						if(foundit)
							badmage = true;
						foundit = true;
						answer = cards2[k+12];
					}
				}
			}
			break;
		default:
			cout << "Something went wrong for Case: " << i << endl;
			break;
		}
		
		cout << "Case #" << i << ": ";
		if(foundit && !badmage)
			cout << answer << endl;
		else if(badmage)
			cout << "Bad magician!" << endl;
		else
			cout << "Volunteer cheated!" << endl;
		
    }
    
  }

  return 0;
}
