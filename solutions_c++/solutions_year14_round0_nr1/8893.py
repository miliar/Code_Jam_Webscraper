#include <iostream>

using namespace std;

#define GRID_SIZE 4

int main() {
	int test_cases, answer_to_first_question, answer_to_second_question;
	int grid[4][4], candidates[4], rows_of_candidates[4], columns_of_candidates[4];
	int row, column, candidate, found;

	cin >> test_cases;
	for (int kase = 1; kase <= test_cases; ++kase) {
		cout << "Case #" << kase << ": ";

		cin >> answer_to_first_question;
		--answer_to_first_question; // Convert to 0-based.

		for (row = 0; row < GRID_SIZE; ++row)
			for (column = 0; column < GRID_SIZE; ++column)
				cin >> grid[row][column];

		for (column = 0; column < GRID_SIZE; ++column)
			candidates[column] = grid[answer_to_first_question][column];

		cin >> answer_to_second_question;
		--answer_to_second_question; // Convert to 0-based.

		for (row = 0; row < GRID_SIZE; ++row)
			for (column = 0; column < GRID_SIZE; ++column)
				cin >> grid[row][column];

		for (row = 0, found = 4; row < GRID_SIZE; ++row)
			for (column = 0; column < GRID_SIZE; ++column)
				for (candidate = 0; candidate < GRID_SIZE; ++candidate)
					if (grid[row][column] == candidates[candidate]) {
						rows_of_candidates[candidate] = row;
						columns_of_candidates[candidate] = column;
						if (0 == --found) // Done!
							goto CHECK_FOR_CHEATER; // Use goto to break from a nested loop.
					}

	CHECK_FOR_CHEATER:
		if (rows_of_candidates[0] != answer_to_second_question &&
			rows_of_candidates[1] != answer_to_second_question &&
			rows_of_candidates[2] != answer_to_second_question &&
			rows_of_candidates[3] != answer_to_second_question) {
				cout << "Volunteer cheated!\n";
				continue;
		}

	CHECK_FOR_GOOD_MAGICIAN:
		// The trick only works if the row that answers the second question contains exactly a single candidate.
		if (rows_of_candidates[row = 0] == answer_to_second_question &&
			rows_of_candidates[1] != answer_to_second_question &&
			rows_of_candidates[2] != answer_to_second_question &&
			rows_of_candidates[3] != answer_to_second_question
			    ||
			rows_of_candidates[row = 1] == answer_to_second_question &&
			rows_of_candidates[0] != answer_to_second_question &&
			rows_of_candidates[2] != answer_to_second_question &&
			rows_of_candidates[3] != answer_to_second_question
			    ||
			rows_of_candidates[row = 2] == answer_to_second_question &&
			rows_of_candidates[0] != answer_to_second_question &&
			rows_of_candidates[1] != answer_to_second_question &&
			rows_of_candidates[3] != answer_to_second_question
			    ||
			rows_of_candidates[row = 3] == answer_to_second_question &&
			rows_of_candidates[0] != answer_to_second_question &&
			rows_of_candidates[1] != answer_to_second_question &&
			rows_of_candidates[2] != answer_to_second_question) {
				cout << candidates[row] << "\n";
				continue;
		}

	CHECK_FOR_BAD_MAGICIAN:
		// We can check here the case for a bad magician: The row that answers the second
		//   question contains multiple candidates. But that is not necessary, since this
		//   is what we are left with anyway...
		cout << "Bad magician!\n";
	}

	return 0;
}