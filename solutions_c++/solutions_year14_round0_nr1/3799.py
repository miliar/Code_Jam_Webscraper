#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>

using namespace std;

int main(void) {
	int cases; cin >> cases;
	int case_number=0;
	const string BAD="Bad magician!";
	const string CHEAT="Volunteer cheated!";

	while (cases-->0) {
		case_number++;

		int answer; cin >> answer;
		vector<int> row(4);
		for (int i=0; i<4; i++) {
			for (int j=0; j<4; j++) {
				int number; cin >> number;
				if (i+1==answer) {
					row[j] = number;
				}
			}
		}

		int answer2; cin >> answer2;
		vector<int> row_2(4);
		for (int i=0; i<4; i++) {
			for (int j=0; j<4; j++) {
				int number; cin >> number;
				if (i+1==answer2) {
					row_2[j] = number;
				}
			}
		}


		vector<int> potential_answers;
		for (int i=0; i<4; i++) {
			for (int j=0; j<4; j++) {
				if (row[i] == row_2[j])
					potential_answers.push_back(row[i]);
			}
		}

		cout << "Case #" << case_number << ": ";
		if (potential_answers.size() == 0) {
			cout << CHEAT << endl;
		}

		else if (potential_answers.size() > 1) {
			cout << BAD << endl;
		}

		else {
			cout << potential_answers[0] << endl;
		}

		
	}
}