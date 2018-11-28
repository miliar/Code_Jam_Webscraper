//============================================================================
// Name        : DeceitfulWar.cpp
// Author      : Xuanchen Tang
// Version     :
// Copyright   : 
// Description : Google Code Jam, Qualification Round 2014, Problem D. Deceitful War
//============================================================================

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
	int caseNumber;
	cin >> caseNumber;

	int blocks;
	int warScore, deceitfulWarScore;
	double weight;
	vector<double> naomi, ken, naomiCopy, kenCopy; // Copies are used for deceitful War
	vector<int> result;
	int smallerThanKenFirst, largerThanNaomiLast, mustLose, size, counter;
	int i, j, k;

	for (i = 0; i < caseNumber; ++i) {
		warScore = 0; deceitfulWarScore = 0;
		naomi.clear(); ken.clear(); result.clear();
		cin >> blocks;
		for (j = 0; j < blocks; ++j) {
			cin >> weight;
			naomi.push_back(weight);
		}
		sort(naomi.begin(), naomi.end());
		naomiCopy = naomi;

		for (j = 0; j < blocks; ++j) {
			cin >> weight;
			ken.push_back(weight);
		}
		sort(ken.begin(), ken.end());
		kenCopy = ken;

		std::vector<double>::iterator p;
		for (j = 0; j < blocks; ++j) {
			p = std::lower_bound(ken.begin(), ken.end(), naomi[j]);
			if (p == ken.end()) {
				warScore++;
				ken.erase(ken.begin());
 			} else {
 				ken.erase(p);
 			}
		}

		p = lower_bound(naomiCopy.begin(), naomiCopy.end(), kenCopy.front());
		smallerThanKenFirst = p - naomiCopy.begin();

		p = upper_bound(kenCopy.begin(), kenCopy.end(), naomiCopy.back());
		largerThanNaomiLast = kenCopy.end() - p;

		mustLose = max(smallerThanKenFirst, largerThanNaomiLast);
		kenCopy.erase(kenCopy.end() - mustLose, kenCopy.end());
		naomiCopy.erase(naomiCopy.begin(), naomiCopy.begin() + mustLose);

		size = blocks - mustLose;
		j = size - 1; k = size - 1;
		while((j >= 0) && (k >= 0)) {
			if (naomiCopy[j] > kenCopy[k]) {
				result.push_back(1);
				--j;
			} else {
				result.push_back(-1);
				--k;
			}
		}
		// Only one of the following is valid
		while (j >= 0) {
			result.push_back(1);
			--j;
		}
		while (k >= 0) {
			result.push_back(-1);
			--k;
		}

		counter = 0;
		for (j = 0; j < 2 * size; ++j){
			counter += result[j];
			if (counter < 0) {
				++mustLose;
				counter = 0;
			}
		}

		deceitfulWarScore = blocks - mustLose;
		cout << "Case #" << i + 1 << ": " << deceitfulWarScore << " " << warScore << endl;
	}

	return 0;
}
