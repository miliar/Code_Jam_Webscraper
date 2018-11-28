#include <iostream>

using namespace std;

/**
 * Reads the next five lines of input for the row the user chose
 * it is up to the caller to delete the int array returned
 * @return returns an int array with four ints, representing the row
 */
int* getRow(){
	int row;
	cin >> row;
	int dummy;
	int * res = new int[4];
	// there are only four rows to expect;
	for (int i = 1; i < 5; i++){
		if (row == i)
			cin >> res[0] >> res[1] >> res[2] >> res[3];
		else
			cin >> dummy >> dummy >> dummy >> dummy;
	}
	return res;
}

/**
 * Processes a case for the problem
 * @param caseNumber the number to output for the solution
 */
void processCase(int caseNumber){
	// get the cards on the row
	int * row1 = getRow();
	int * row2 = getRow();

	// the potential solution
	int card;
	// number of potential matches
	int numpotential=0;

	// doing a 4*4 search, sloopy
	for (int i = 0; i < 4; i++){
		for(int j = 0; j < 4; j++){
			if (row1[i] == row2[j]){
				// get the card that exists in both set
				card = row1[i];
				numpotential++;
			}
		}
	}

	cout << "Case #" << caseNumber << ": ";
	// the mage fails
	if (numpotential > 1)
		cout << "Bad magician!" << endl;
	// only one match, therefore the card is the correct one
	else if (numpotential == 1)
		cout << card << endl;
	// there are no matches between the rows
	else
		cout << "Volunteer cheated!" << endl;

	//delete rows
	delete [] row1;
	delete [] row2;
}

int main (void) {
	int numCases;
	cin >> numCases;
	numCases++;
	for (int i = 1;  i < numCases; i++) {
		processCase(i);
	}
	return 0;
}

