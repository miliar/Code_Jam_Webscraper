// Author: Death.Light

#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

int one, two, cnt, res;
int a[4][4], b[4][4];

void write () {
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) cout << a[i][j] << " ";
		cout << endl;
	}
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) cout << b[i][j] << " ";
		cout << endl;
	}	
}

void testcase (int numtest) {
	cin >> one;
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++) cin >> a[i][j];
	cin >> two;
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++) cin >> b[i][j];
	cnt = 0;
	for (int i = 0; i < 4; i++)	
		for (int j = 0; j < 4; j++)
			if (a[one - 1][i] == b[two - 1][j]) {
				cnt++;
				res = a[one - 1][i];
			}
	printf ("Case #%d: ", numtest);
	if (cnt == 1) printf ("%d", res);
	else if (cnt == 0) printf ("Volunteer cheated!");
	else printf ("Bad magician!");
	printf ("\n");
}

int main () {
	freopen ("Death.Light", "r", stdin);
	freopen ("Light.Death", "w", stdout);
	int test;
	cin >> test;
	for (int i = 1; i <= test; i++) testcase (i);
  return 0;
}

