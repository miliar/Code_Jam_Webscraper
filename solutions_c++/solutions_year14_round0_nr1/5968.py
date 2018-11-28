#include <iostream>
using namespace std;

int main() {
	int num_test_cases;
	//volunteer cheated if all the numbers in the first choice do not appear in the second choice
	//bad magician if more than 1 number in the first row appeared in the second row
	//choose a number in any row, now split the numbers in that row across all the other rows (you can do it in any way)
	//simply find the number in the new row
	cin >> num_test_cases;
	int grid[4][4];
	//int count = 1;

	for (int i = 1; i <= num_test_cases; ++i) {
		int first_choice;
		cin >> first_choice; first_choice--; cin.ignore();
		int first_choice_picks[4];

		for (int x = 0; x < 4; ++x) {
			for (int y = 0; y < 4; ++y) {
				cin >> grid[x][y];
			}
			cin.ignore();
		}
		for (int x = 0; x < 4; ++x) {
			first_choice_picks[x] = grid[first_choice][x];
		}
		
		/*cout << "Printing First Grid...\n";
		for (int x = 0; x < 4; ++x) {
			for (int y = 0; y < 4; ++y) {
				cout << grid[x][y] <<  " ";
			}
			cout << endl;
		}*/

		int second_choice; cin >> second_choice; second_choice--;
		//reading in second grid
		for (int x = 0; x < 4; ++x) {
			for (int y = 0; y < 4; ++y) {
				cin >> grid[x][y];
			}
			cin.ignore();
		}

		/*cout << "Printing Second Grid...\n";
		for (int x = 0; x < 4; ++x) {
			for (int y = 0; y < 4; ++y) {
				cout << grid[x][y] <<  " ";
			}
			cout << endl;
		}*/

		int count = 0; int answer;
		for (int a = 0; a < 4; ++a) {
			for (int b = 0; b < 4; ++b) {
				if (grid[second_choice][a] == first_choice_picks[b]) {
					count++;
					answer = grid[second_choice][a];
				}
			}
		}

		if (count == 0) {
			cout << "Case #" << i << ": Volunteer cheated!" << endl;
		} else if (count == 1) {
			cout << "Case #" << i << ": " << answer << endl;
		} else {
			cout << "Case #" << i << ": Bad magician!" << endl;
		}

	}
}