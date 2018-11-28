#include <iostream>

int main(int argc, char** argv) {

	int t = 0;
	int guess1, guess2;
	int cards1[16], cards2[16];
	int row1[4], row2[4];

	int card, numcards;

	std::cin >> t;

	for(int i = 0; i < t; i++) {
		card = numcards = 0;

		std::cin >> guess1;
		guess1--;
		for(int j = 0; j < 16; j++) {
			std::cin >> cards1[j];
		}

		std::cin >> guess2;
		guess2--;
		for(int j = 0; j < 16; j++) {
			std::cin >> cards2[j];
		}

		for(int j = 0; j < 4; j++) {
			row1[j] = cards1[guess1 * 4 + j];
		}

		for(int j = 0; j < 4; j++) {
			row2[j] = cards2[guess2 * 4 + j];
		}
		
		for(int j = 0; j < 4; j++) {
			for(int k = 0; k < 4; k++) {
				if(row1[j] == row2[k]) {
					card = row1[j];
					numcards++;
				}
			}			
		}

		if(numcards == 0)
			std::cout << "Case #" << i+1 << ": Volunteer cheated!" << std::endl;
		else if(numcards == 1)
			std::cout << "Case #" << i+1 << ": " << card << std::endl;
		else
			std::cout << "Case #" << i+1 << ": Bad magician!" << std::endl;
	}

}