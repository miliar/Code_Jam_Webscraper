#include <set>
#include <iostream>
using namespace std;

set<int> choices;
int T, caso, aux, row, qtt, res;

int main() {
	ios_base::sync_with_stdio(false);
	cin >> T;
	for (caso=1; caso<=T; caso++) {
		choices.clear(); qtt = 0;
		cin >> row;

		for (int i=1; i<=4; i++)
			for (int j=1; j<=4; j++) {
				cin >> aux;
				if (i == row)
					choices.insert(aux);
			}

		cin >> row;

		for (int i=1; i<=4; i++)
			for (int j=1; j<=4; j++) {
				cin >> aux;
				if (i==row && choices.count(aux)) {
					qtt++;
					res = aux;
				}

			}

		cout << "Case #" << caso << ": ";
		if (qtt == 1)
			cout << res << "\n";
		else if (qtt == 0)
			cout << "Volunteer cheated!\n";
		else
			cout << "Bad magician!\n";
	}
}