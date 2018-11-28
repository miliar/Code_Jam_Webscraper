#include	<iostream>
#include	<ostream>
#include	<set>
using namespace std;

int main(void) {
	int T; cin >> T;

	for (int t = 1; t <= T; ++t) {
		int ans1, ans2;
		int	deck1[4][4], deck2[4][4];

		cin >> ans1;
		--ans1;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				cin >> deck1[i][j];

		cin >> ans2;
		--ans2;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				cin >> deck2[i][j];

		set<int>	candidates(deck1[ans1], deck1[ans1] + 4);
		set<int>	choosen;
		for (int i = 0; i < 4; ++i)
			if (candidates.count(deck2[ans2][i]))
				choosen.insert(deck2[ans2][i]);

		cout << "Case #" << t << ": ";
		switch (choosen.size()) {
			case 1:
				cout << *choosen.begin();
				break;
			case 0:
				cout << "Volunteer cheated!";
				break;
			default:
				cout << "Bad magician!";
				break;
		}
		cout << endl;
	}

	return 0;
}