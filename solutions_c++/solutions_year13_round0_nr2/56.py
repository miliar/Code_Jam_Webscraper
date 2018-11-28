#include <iostream>
#include <algorithm>


int main()
{
	int T;

	// Read the number of cases
	std::cin >> T;

	// For each case
	for (int t = 0 ; t < T ; t++) {
		int N, M;

		// Read the case
		std::cin >> N >> M;
		int *test_case = new int[N*M];
		for (int i = 0, k = 0 ; i < N ; i++) {
			for (int j = 0 ; j < M ; j++, k++) {
				std::cin >> test_case[k];
			}
		}

		// Compute maximum of each row/columns
		int *row_max = new int[N], *col_max = new int[M];
		for (int i = 0 ; i < N ; i++) {
			row_max[i] = 0;
		}

		for (int j = 0 ; j < M ; j++) {
			col_max[j] = 0;
		}

		for (int i = 0, k = 0 ; i < N ; i++) {
			for (int j = 0 ; j < M ; j++, k++) {
				row_max[i] = std::max(row_max[i], test_case[k]);
				col_max[j] = std::max(col_max[j], test_case[k]);
			}
		}

		// Check that each tile is greater or equal (that is, equal) to the maximum of row or column
		bool result = true;

		for (int i = 0, k = 0 ; i < N ; i++) {
			for (int j = 0 ; j < M ; j++, k++) {
				if (test_case[k] < row_max[i] && test_case[k] < col_max[j]) {
					result = false;
					break;
				}
			}

			if (!result) { // Shortcut
				break;
			}
		}


		// Print the result
		std::cout << "Case #" << (t+1) << ": ";

		if (result)
			std::cout << "YES";
		else
			std::cout << "NO";

		std::cout << std::endl;

		delete [] test_case;
		delete [] row_max;
		delete [] col_max;
	}

	return 0;
}
