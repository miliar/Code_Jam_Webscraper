#include <vector>
#include <cstdio>
#include <iostream>
#include <set>

using namespace std;

int a1[4][4];
int a2[4][4];

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int T;
	cin >> T;
	for (int t=0; t<T; t++) {
		int firstR;
		cin >> firstR;
		for (int r=0; r<4; r++)
			for (int c=0; c<4; c++)
				cin >> a1[r][c];
		int secondR;
		cin >> secondR;
		for (int r=0; r<4; r++)
			for (int c=0; c<4; c++)
				cin >> a2[r][c];
		set<int> row1;
		for (int c=0; c<4; c++)
			row1.insert(a1[firstR-1][c]);
		vector<int> founds;
		for (int c=0; c<4; c++)
			if (row1.count(a2[secondR-1][c]))
				founds.push_back(a2[secondR-1][c]);
		if (founds.size() == 0)
			printf("Case #%d: Volunteer cheated!\n", t+1);
		else if (founds.size() == 1)
			printf("Case #%d: %d\n", t+1, founds[0]);
		else 
			printf("Case #%d: Bad magician!\n", t+1);
	}

	return 0;
}