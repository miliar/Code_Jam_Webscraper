#include <iostream>
#include <string>
#include <vector>
#include <sstream> 

using namespace std;

int main() {
	
// taking inputs
	int no_cases;
	cin >> no_cases;
	int matches = 0;
	
	for (int cases = 0; cases < no_cases; cases++) {
		// filling matrices;
		stringstream output;
		int first_choice;
		vector<int> first_choice_row;
		cin >> first_choice;

		vector<vector< int > > matrix1(4, vector< int >(4));
	
		for (int row = 0; row < 4; row++) {
			for (int col = 0; col < 4; col++) {
				cin >> matrix1[row][col];
			}
		}
		for (int i = 0; i < 4; i++) {
			first_choice_row.push_back(matrix1[first_choice - 1][i]);
		}

		int second_choice;
		vector<int> second_choice_row;
		cin >> second_choice;

		vector<vector< int > > matrix2(4, vector< int >(4));
		for (int row = 0; row < 4; row++) {
			for (int col = 0; col < 4; col++) {
				cin >> matrix2[row][col];
			}
		}
		for (int i = 0; i < 4; i++) {
			second_choice_row.push_back(matrix2[second_choice - 1][i]);
		}
		int match;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (first_choice_row[i] == second_choice_row[j]) {
					matches++;
					match = first_choice_row[i];
				}
			}
		}
		if (matches == 0) {
			output << "Case #"<< cases + 1 << ": " << "Volunteer cheated!";
		} else if (matches == 1) {
			output << "Case #" << cases+1 << ": " << match;
		}
		else if (matches > 1) {
			output << "Case #" << cases + 1 << ": " << "Bad magician!";
		}
		if (cases == no_cases -1) {
			cout << output.str();
		}
		else {
			cout << output.str() << '\n';
		}
		matches = 0;
	}
	return 0;
}
