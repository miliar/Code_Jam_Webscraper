#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(void) {
	int numCases;
	
	cin >> numCases;
	for (int numCase = 1; numCase <= numCases; numCase++) {
		int answer, card;
		vector<int> firstPossibilities, secondPossibilities, matches;
		
		cin >> answer;
		for (int i = 1; i <= 4; i++) {
			for (int j = 1; j <= 4; j++) {
				cin >> card;
				
				if (i == answer) {
					firstPossibilities.push_back(card);
				}
			}
		}
		
		cin >> answer;
		for (int i = 1; i <= 4; i++) {
			for (int j = 1; j <= 4; j++) {
				cin >> card;
				
				if (i == answer) {
					secondPossibilities.push_back(card);
				}
			}
		}

		sort(firstPossibilities.begin(), firstPossibilities.end());
		sort(secondPossibilities.begin(), secondPossibilities.end());
		set_intersection (firstPossibilities.begin(), firstPossibilities.end(), secondPossibilities.begin(), secondPossibilities.end(), back_inserter(matches));
		
		cout << "Case #" << numCase << ": ";
		if (matches.size() == 0) {
			cout << "Volunteer cheated!" << endl;
		} else if (matches.size() == 1) {
			cout << matches[0] << endl;
		} else {
			cout << "Bad magician!" << endl;
		}
	}
}
