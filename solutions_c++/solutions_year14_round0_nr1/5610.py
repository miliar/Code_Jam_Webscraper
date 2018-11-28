#include<vector>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;

int main() {
	int t, case_num=0;
	int cards[4][4];
	int possible_cards[4];
	int matches = 0;
	int solution;
	scanf("%d", &t);
	while (t--) {
		int n1, n2;
		case_num++;
		matches = 0;
		scanf("%d", &n1);
		for (int j=0; j<4; j++)
			for (int i=0; i<4; i++)
				scanf("%d", &cards[j][i]);

		for (int i=0; i<4; i++)
			possible_cards[i] = cards[n1-1][i];

		scanf("%d", &n2);
		for (int j=0; j<4; j++)
			for (int i=0; i<4; i++)
				scanf("%d", &cards[j][i]);

		for (int i=0; i<4; i++)
		{
			for (int j=0; j<4; j++)
				if (possible_cards[i] == cards[n2-1][j])
				{
					solution = possible_cards[i];
					matches++;
				}
		}

		if (matches == 1)
			printf("Case #%d: %d\n", case_num, solution);
		else if (matches > 1)
			printf("Case #%d: Bad magician!\n", case_num, solution);
		else
			printf("Case #%d: Volunteer cheated!\n", case_num, solution);
	}
	return 0;
}
