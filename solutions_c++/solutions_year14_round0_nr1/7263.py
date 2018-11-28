#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <time.h>
#include <math.h>
#include <iostream>



using namespace std;

int main() {
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("res.txt", "w", stdout);
	int t;
	cin >> t;
	for (int k = 0; k < t; k++) {
		int ans1;
		cin >> ans1;
		int a1[4];
		for (int l = 0; l < ans1; l++) {
			for (int i = 0; i < 4; i++) {
				cin >> a1[i];
			}
		}
		int x;
		for (int l = 0; l < 4-ans1; l++) {
			for (int i = 0; i < 4; i++) {
				cin >> x;
			}
		}
		int ans2;
		cin >> ans2;
		int a2[4];
		for (int l = 0; l < ans2; l++) {
			for (int i = 0; i < 4; i++) {
				cin >> a2[i];
			}
		}
		for (int l = 0; l < 4 - ans2; l++) {
			for (int i = 0; i < 4; i++) {
				cin >> x;
			}
		}
		int c = 0;
		int res = 1;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (a1[i] == a2[j]) {
					c++;
					res = a1[i];
				}
			}
		}
		if (c == 1) {
			cout << "Case #" << k + 1 << ": "<< res;
		}
		else if (c == 0) {
			cout << "Case #" << k + 1<< ": Volunteer cheated!";
		}
		else {
			cout << "Case #"<<k+1<<": Bad magician!";
		}
		cout << '\n';
	}
	return 0;
}