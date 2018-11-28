#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>

using namespace std;

const double delta = 0.0000001;

int calculate_deceitful_score_2(vector<double> naomi, vector<double> ken) {
	int i=0;
	int j=0;

	int score=0;

	while (i<naomi.size() && j<ken.size()) {
		if (naomi[i] > ken[j]) {
			i++;
			j++;
			
			score++;
		}
		else {
			i++;
		}
	}

	return score;
}


int calculate_deceitful_score(vector<double> naomi, vector<double> ken) {
	if (naomi.size() == 0) return 0;

	int max_score = 0;

	for (int i=0; i<naomi.size(); i++) {
		for (int j=0; j<ken.size(); j++) {
			if (ken[j] > naomi[i]) {
				vector<double> ken_2 = ken;
				ken_2.erase(ken_2.begin()+j);

				vector<double> naomi_2 = naomi;
				naomi_2.erase(naomi_2.begin()+i);

				int recursion = calculate_deceitful_score(naomi_2,ken_2);
				max_score = max(recursion, max_score);
			}

			else {
				vector<double> ken_2 = ken;
				ken_2.erase(ken_2.begin()+j);

				vector<double> naomi_2 = naomi;
				naomi_2.erase(naomi_2.begin()+i);

				int recursion = 1+calculate_deceitful_score(naomi_2,ken_2);
				max_score = max(recursion, max_score);
			}
		}
	}


	return max_score;
}

int calculate_optimal_score(vector<double> naomi, vector<double> ken) {
	if (naomi.size() == 0) return 0;

	double N = naomi[naomi.size()-1];
	naomi.erase(naomi.begin()+naomi.size()-1);

	bool ken_wins = false;
	for (int i=0; i<ken.size(); i++) {
		if (ken[i] > N) {
			ken_wins = true;
			ken.erase(ken.begin()+i);
			break;
		}
	}

	if (ken_wins)
		return calculate_optimal_score(naomi, ken);
	else
		return 1+calculate_optimal_score(naomi,ken);
}

int main(void) {
	int cases; cin >> cases;
	int case_number=0;

	while (cases-->0) {
		case_number++;

		int blocks; cin >> blocks;

		vector<double> naomi(blocks);
		vector<double> ken(blocks);

		for (int i=0; i<blocks; i++) {
			cin >> naomi[i];
		}

		sort(naomi.begin(), naomi.end()); // descending

		for (int i=0; i<blocks; i++) {
			cin >> ken[i];
		}
		sort(ken.begin(), ken.end());

		int opt = calculate_optimal_score(naomi,ken);
		int opt_d = calculate_deceitful_score_2(naomi,ken);

		cout << "Case #" << case_number << ": " << opt_d << " " << opt << endl;

		
	}
}
