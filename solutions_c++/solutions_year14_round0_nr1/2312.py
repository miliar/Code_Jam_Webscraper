#include <iostream>
#include <vector>
using namespace std;

void skip() {
	int ignore;
	for(int counter = 1; counter <= 4; ++counter)
		cin >> ignore;
}

int main() {
	int tests, row, card;
	cin >> tests;
	vector<int> cards(4);
	for(int test = 1; test <= tests; ++test) {
		cin >> row;
		for(int counter = 1; counter < row; ++counter)
			skip();
		for(int& card : cards)
			cin >> card;
		for(int counter = row + 1; counter <= 4; ++counter)
			skip();
		cin >> row;
		for(int counter = 1; counter < row; ++counter)
			skip();
		int solution = 0;
		for(int counter = 1; counter <= 4; ++counter) {
			cin >> card;
			for(int other : cards)
				if(card == other) {
					if(solution)
						solution = -1;
					else
						solution = card;
					break;
				}
		}
		for(int counter = row + 1; counter <= 4; ++counter)
			skip();
		cout << "Case #" << test << ": ";
		if(solution < 0)
			cout << "Bad magician!\n";
		else if(solution)
			cout << solution << '\n';
		else
			cout << "Volunteer cheated!\n";
		
	}
	return 0;
}
