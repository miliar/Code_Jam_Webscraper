#include <stdio.h>
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>

using namespace std;
class rowCards {
	public:
		bool addCards(int n1, int n2, int n3, int n4);
		int getCard(int n);
		int compare(rowCards* row1, rowCards* row2);
		int getCommon();
	private:
		int cards[4];
		int commonCard;
};

bool rowCards::addCards(int n1, int n2, int n3, int n4) {
	int i, inputs[4] = {n1, n2, n3, n4};
	for (i=0; i<4; i++) {
		cards[i] = inputs[i];
	}
	return true;
}

int rowCards::getCard (int n) { return cards[n]; }

int rowCards::getCommon() { return commonCard; }

int rowCards::compare(rowCards* row1, rowCards* row2) {
	int count = 0, j, k;
	for (j = 0; j<4; j++) {
		for (k = 0; k<4; k++) {
			if ((*row1).getCard(j) == (*row2).getCard(k)) {
				commonCard = (*row1).getCard(j);
				count++;
			}
		}
	}
	return count;
}

void main() {
	ifstream myFile;
	myFile.open("data.txt");

	ofstream outFile;
	outFile.open("out.txt");

	int numCases = 0;
	int answer1 = 0, answer2 = 0;
	int n1,n2,n3,n4, i;
	int common = 0;
	int four = 4;
	int curCase = 1;
	rowCards cards1, cards2;

	myFile >> numCases;
	string trash;

	while (numCases--) {
		four = 4;
		myFile >> answer1;
		while (answer1-- != 0) {
			myFile >> n1 >> n2 >> n3 >> n4;
			four --;
		}
		cards1.addCards(n1, n2, n3, n4);
		
		while (four-- >= 1) {
			myFile >> n1 >> n2 >> n3 >> n4;
		}
		
		four = 4;
		myFile >> answer2;
		while (answer2-- != 0) {
			myFile >> n1 >> n2 >> n3 >> n4;
			four--;
		}
		cards2.addCards(n1, n2, n3, n4);

		while (four-- >= 1) {
			myFile >> n1 >> n2 >> n3 >> n4;
		}

		common = cards1.compare(&cards1, &cards2);
		
		if (common == 1) {
			//found! output common
			cout	<< "Case #" << curCase << ": " << cards1.getCommon() << endl;
			outFile << "Case #" << curCase << ": " << cards1.getCommon() << endl;
		} else if (common == 0) {
			//Volunteer Cheated!
			cout	<< "Case #" << curCase << ": " << "Volunteer cheated!" << endl;
			outFile << "Case #" << curCase << ": " << "Volunteer cheated!" << endl;

		} else {
			// Bad magician!
			cout	<< "Case #" << curCase << ": " << "Bad magician!" << endl;
			outFile << "Case #" << curCase << ": " << "Bad magician!" << endl;
		}
		curCase++;
	}

	system("pause");

}