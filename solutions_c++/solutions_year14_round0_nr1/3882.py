#include <iostream>
#include <algorithm>    // std::sort
#include <vector>  
#include <stdio.h>
using namespace std;

void solve()
{
	int r1, r2;
	int c1[4], c2[4];
	int idx = 0;
	int c;
	cin >> r1;
	for (int i=0; i<4; i++) {
		for (int j=0; j<4; j++) {
			cin >> c;
			if (r1 == i+1) {
				c1[idx++] = c;
			}
		}
	}
	idx = 0;
	cin >> r2;
	for (int i=0; i<4; i++) {
		for (int j=0; j<4; j++) {
			cin >> c;
			if (r2 == i+1) {
				c2[idx++] = c;
			}
		}
	}

	int count[17] = {0};
	
	for (int i=0; i<4; i++) {
		count[c1[i]]++;
		count[c2[i]]++;
	}

	int num = 0;
	for (int i=1; i<=16; i++) {
		if (count[i] == 2) {
			if (num == 0) {
				num = i;
			} else {
				cout << "Bad magician!";
				return;
			}
		}
	}

	if (num == 0) {
		cout << "Volunteer cheated!";
	} else {
		cout << num;
	}

	return;
}

int main() {
	int T;

	cin >> T;

	for (int i=1; i<=T; i++) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
	// your code goes here
	return 0;
}
