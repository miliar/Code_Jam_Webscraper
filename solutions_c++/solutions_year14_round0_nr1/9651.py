#include "stdafx.h"
#include <iostream>
#include <cmath>
#include <ctime>
#include <vector>
#include <fstream>

int main()
{
	using namespace std;
	int delay;
	time_t start_time = time(NULL);
	time_t end_time;



	int cases;
	int ans_A;
	int ans_B;
	int cards[4][4];
	int selected[4];
	bool isBadMagic = false;
	bool isBadCards = false;
	int chosen_card = 0;
	string line;
	ifstream input("input.in");
	ofstream output("output.txt");
	
	input >> cases;
	for (int i=0; i<cases; ++i) {
		input >> ans_A;
		for (int row=0; row<4; ++row) {
			for (int col=0; col<4; ++col) {
				input >> cards[row][col]; // read all cards first time
			}
		}
		input >> ans_B;
		for (int col=0; col<4; ++col) {
			selected[col] = cards[ans_A-1][col]; // record the first possibilities
		}

		for (int row=0; row<4; ++row) {
			for (int col=0; col<4; ++col) {
				input >> cards[row][col]; // read all cards second time
			}
		}
		isBadMagic = false;
		isBadCards = false;
		chosen_card = 0;
		for (int col=0; col<4; ++col) {
			for (int i=0; i<4; i++) {
				if (cards[ans_B-1][col] == selected[i]) {
					if (chosen_card == 0) {
						chosen_card = selected[i];
					} else {
						isBadMagic = true;
					}
				}
			}
		}
		if (chosen_card == 0) {
			isBadCards = true;
		}

		output << "Case #" << i+1 << ": ";
		if (isBadCards == true) {
			output << "Volunteer cheated!\n";
		} else if (isBadMagic == true) {
			output << "Bad magician!\n";
		} else {
			output << chosen_card << endl;
		}
	}



	end_time = time(NULL);
	//std::cout << "Ran for " << difftime(end_time, start_time) << " seconds." << endl;
	//std::cin >> delay;
	return 0;
}
