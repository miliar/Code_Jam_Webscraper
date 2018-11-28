#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <string>

using namespace std;

int main(int argc, char* argv[]) {
	// initialize variables
	vector<vector<int> > cards_one;
	vector<vector<int> > cards_two;
	vector<int> rows;
	
	int num_cases;
	int number;
	int guess_one;
	int guess_two;
	
	// Get number of inputs
	cin >> num_cases;
	
	int i = 1;
	do {
		// get answer to first q
		cin >> guess_one;
		// get card arrangement
		for(int x = 0; x < 4; ++x) {
			for(int y = 0; y < 4; ++y) {
				cin >> number;
				rows.push_back(number);
			}
			cards_one.push_back(rows);
			rows.clear();
		}
		
		rows.clear();
		// get answer to the second q
		cin >> guess_two;
		// get card arrangement
		for(int x = 0; x < 4; ++x) {
			for(int y = 0; y < 4; ++y) {
				cin >> number;
				rows.push_back(number);
			}
			cards_two.push_back(rows);
			rows.clear();
		}

		
		vector<int> row_one = cards_one[guess_one-1];
		vector<int> row_two = cards_two[guess_two-1];
		
		bool found = false;
		int num_found = 0;
		
		int answer;
		for(int x = 0; x < 4; ++x) {
			for(int y = 0; y < 4; ++y) {
				if(row_one[x] == row_two[y]) {
					found = true;
					answer = row_one[x];
					++num_found;
				}
			}
		}
		
		if(found && num_found == 1) {
			// if guess is right		
			cout << "Case #" << i << ": " << answer << endl;
		}
		else if(num_found > 1) {
			//
			cout << "Case #" << i << ": " << "Bad magician!" << endl;
		}
		else if(num_found == 0 && !found){
			//
			cout << "Case #" << i << ": " << "Volunteer cheated!" << endl;
		}
		
		rows.clear();
		cards_one.clear();
		cards_two.clear();
		--num_cases;
		++i;
	} while(num_cases > 0);
	

	return 0;
}