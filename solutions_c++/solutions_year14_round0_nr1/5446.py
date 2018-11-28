#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

int T;

int first_cards[4][4];
int second_cards[4][4];

int main()
{
	cin >> T;
	for (int t = 0; t < T; t++) {
		int fr, sr;
		cin >> fr; fr--;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				cin >> first_cards[i][j];
		cin >> sr; sr--;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				cin >> second_cards[i][j];

		vector<int> cs;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				if (first_cards[fr][i] == second_cards[sr][j])
					cs.push_back(first_cards[fr][i]);

		printf("Case #%d: ", t+1);
		if (cs.size() == 0) {
			printf("Volunteer cheated!\n");
		} else if (cs.size() == 1) {
			printf("%d\n", cs[0]);
		} else if (cs.size() > 1) {
			printf("Bad magician!\n");
		}
	}
	return 0;
}
