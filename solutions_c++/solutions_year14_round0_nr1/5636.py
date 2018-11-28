#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;
#define FOR(i, a, b) for(int i = a; i <= b; i ++) 

int a[10][10], b[10][10], test, i1, i2, cc, rr;

int main() {
	freopen("test.inp", "r", stdin);
	freopen("test.out", "w", stdout);
	
	cin >> test;
	FOR(t, 1, test) {
		printf("Case #%d: ", t);
		cin >> i1;
		FOR(i, 1, 4) FOR(j, 1, 4) scanf("%d", &a[i][j]);
		cin >> i2;
		FOR(i, 1, 4) FOR(j, 1, 4) scanf("%d", &b[i][j]);
		cc = 0, rr = 0;
		FOR(i, 1, 4) FOR(j, 1, 4) {
			if (a[i1][i] == b[i2][j]) cc++, rr=a[i1][i];
		}
		if (cc == 0) printf("Volunteer cheated!\n");
		else if (cc > 1) printf("Bad magician!\n");
		else cout << rr << endl;
	}
	return 0;
}