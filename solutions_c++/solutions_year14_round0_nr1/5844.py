#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int T, F, S, CCnt = 0;

	cin >> T;

	while (CCnt < T) {
		cin >> F;
		int C1[16] = {0};
		for (int i = 0; i < 16; i++) {
			int card;
			cin >> card;
			if (i / 4 + 1 == F) {
				C1[card - 1] = 1;
			}
		}
		cin >> S;
		vector <int> CommonCards;
		for (int i = 0; i < 16; i++) {
			int card;
			cin >> card;
			if (i / 4 + 1 == S) {
				if (C1[card - 1] == 1) {
					CommonCards.push_back(card);
				}
			}
		}
		cout << "Case #" << ++CCnt << ": ";
		if (CommonCards.size() == 1) {
			cout << CommonCards[0] << endl;
		} else if (CommonCards.size() > 1) {
			cout << "Bad magician!\n";
		} else {
			cout << "Volunteer cheated!\n";
		}
	}

	return 0;
}
