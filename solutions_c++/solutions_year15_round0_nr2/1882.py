#include <iostream>
#include <vector>
using namespace std;

#define MAX_PANCAKE 1000

int main (void) {
	int nb_case; cin >> nb_case;
	
	for (int c = 0; c < nb_case; ++c) {
		// ubpn[i] = nb users with i pancakes
		vector<int> users_by_pancake_number (MAX_PANCAKE + 1, 0);
		int max_pancake = 0;

		int nb_guys; cin >> nb_guys;
		for (int i = 0; i < nb_guys; ++i) {
			int p; cin >> p;
			users_by_pancake_number[p]++;
			max_pancake = p > max_pancake ? p : max_pancake;
		}

		// compute
		int best_time = MAX_PANCAKE + 1;
		for (int target_pancake = max_pancake; target_pancake >= 1; --target_pancake) {
			// determine how much splits are needed to put everyone under 'target_pancake' pancakes
			int nb_splits = 0;

			for (int p = target_pancake + 1; p <= max_pancake; ++p) {
				int nb_user_with_p_pancakes = users_by_pancake_number[p];
				if (nb_user_with_p_pancakes > 0) {
					int nb_division = (p + target_pancake - 1) / target_pancake;
					int splits = nb_division - 1;
					nb_splits += splits * nb_user_with_p_pancakes;
				}
			}

			int time = target_pancake + nb_splits;
			best_time = time < best_time ? time : best_time;
		}

		cout << "Case #" << c + 1 << ": " << best_time << endl;
	}

	return 0;
}
