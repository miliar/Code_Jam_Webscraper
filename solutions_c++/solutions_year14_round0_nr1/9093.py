#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int t, a1, a2;
int v[17];
int x;
int main() {
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		int c2 = 0;
		int p = -1;
		memset(v, 0, sizeof v);
		scanf("%d", &a1);
		for (int i1 = 1; i1 <= 4; i1++) {
			for (int j1 = 1; j1 <= 4; j1++) {
				scanf("%d", &x);
				if (i1 == a1) {
					v[x]++;
					if (v[x] == 2) {c2++; p = x;}
				}
			}
		}
		scanf("%d", &a2);
		for (int i2 = 1; i2 <= 4; i2++) {
			for (int j2 = 1; j2 <= 4; j2++) {
				scanf("%d", &x);
				if (i2 == a2) {
					v[x]++;
					if (v[x] == 2) {c2++; p = x;}
				}
			}
		}

		printf("Case #%d: ", i);
		if (c2 == 0) {
			cout << "Volunteer cheated!";
		} else if (c2 == 1) {
			cout << p;
		} else {
			cout << "Bad magician!";
		}
		cout << endl;
	}
	return 0;
}
