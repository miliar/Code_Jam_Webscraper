#include <iostream>
#include <fstream>
#include <map>
using namespace std;

int main()
{
	ofstream output("ans.txt");
	int test_cases, cur_case;
	cin >> test_cases;

	int matrix[5][5];

	for (cur_case = 1; cur_case <= test_cases; cur_case++) {
		map<int, int> choice_cards;
		int first_answear;
		cin >> first_answear;

		for (int i = 1; i <= 4; i++) {
			for (int j = 1; j <= 4; j++) {
				cin >> matrix[i][j];
			}
		}

		for (int j = 1; j <= 4; j++) {
			choice_cards[matrix[first_answear][j]] = 1;
		}

		int second_answear;
		cin >> second_answear;

		for (int i = 1; i <= 4; i++) {
			for (int j = 1; j <= 4; j++) {
				cin >> matrix[i][j];
			}
		}
		map<int, int>::iterator it;
		for (int j = 1; j <= 4; j++) {
			it = choice_cards.find(matrix[second_answear][j]);
			if (it != choice_cards.end()) {
				choice_cards[matrix[second_answear][j]] += 1;
			}
			else {
				choice_cards[matrix[second_answear][j]] = 1;
			}
		}

		int ans = -1;
		int num_of_one = 0;
		int num_of_two = 0;

		for (it = choice_cards.begin(); it != choice_cards.end(); it++) {
			if (it->second == 1) {
				num_of_one += 1;
			}
			else {
				num_of_two += 1;
				ans = it->first;
			}
		}

		if (num_of_two == 1) {
			output << "Case #" << cur_case << ": " << ans << endl;
		}
		else if (num_of_two > 1) {
			output << "Case #" << cur_case << ": " << "Bad magician!" << endl;
		}
		else if (num_of_two == 0) {
			output << "Case #" << cur_case << ": " << "Volunteer cheated!" << endl;
		}

	}
}