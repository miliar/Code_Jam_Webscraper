#include <iostream>
#include <cstdio>
#include <set>
using namespace std;

int main() {
	int tn, ti;
	int r, a[10][10];

	cin >> tn;
	for (ti = 0; ti < tn; ti ++) {
		cin >> r;
		for (int i = 0; i < 4; i ++)
		for (int j = 0; j < 4; j ++)
			cin >> a[i][j];
		set<int> s;
		for (int i = 0; i < 4; i ++) {
			s.insert(a[r-1][i]);
		}
		cin >> r;
		for (int i = 0; i < 4; i ++)
		for (int j = 0; j < 4; j ++)
			cin >> a[i][j];
		set<int>S;
		for (int i = 0; i < 4; i ++) {
			if (s.find(a[r-1][i]) != s.end()) {
				S.insert(a[r-1][i]);
			}
		}
		printf("Case #%d: ", ti + 1);
		if (S.size() == 1) {
			printf("%d\n", *S.begin());
		} else if (S.size() > 1) {
			printf("Bad magician!\n");
		} else {
			printf("Volunteer cheated!\n");
		}
	}
	return 0;
}
