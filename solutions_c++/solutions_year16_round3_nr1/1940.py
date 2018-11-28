#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <cmath>

using namespace std;

typedef pair<int, int> P;

int main() {
	int t;
	cin >> t;
	string abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	for (int i = 0; i < t; i++) {
		int n;
		cin >> n;
		vector<int> p(n);
		for (int j = 0; j < n; j++) {
			cin >> p[j];
		}
		printf("Case #%d:", i+1);
		P MAX, SEC;
		while (true) {
			int sum = 0;
			if (p[0] > p[1]) {
				MAX.first = p[0];
				MAX.second = 0;
				SEC.first = p[1];
				SEC.second = 1;
			} else {
				MAX.first = p[1];
				MAX.second = 1;
				SEC.first = p[0];
				SEC.second = 0;
			}
			if (p[0] == 1) {
				sum++;
			}
			if (p[1] == 1) {
				sum++;
			}
			/*for (int j = 0; j < n; j++) {
				cout << p[j] << ' ' ;
			}*/
			//cout << endl;
			for (int j = 2; j < n; j++) {
				if (p[j] > MAX.first) {
					SEC = MAX;
					MAX.first = p[j];
					MAX.second = j;
				} else if (p[j] <= MAX.first) {
					if (p[j] > SEC.first) {
						SEC.first = p[j];
						SEC.second = j;
					}
				}
				if (p[j] == 1) {
					sum++;
				}
			}
			if (MAX.first == 0 && SEC.first == 0) {
				break;
			} else {
				if (MAX.first > SEC.first) {
					printf(" %c", abc[MAX.second]);
					p[MAX.second]--;
				} else if (MAX.first == 1 && SEC.first == 1) {
					if (sum % 2 == 1) {
						printf(" %c", abc[MAX.second]);
						p[MAX.second]--;
					} else {
						printf(" %c%c", abc[MAX.second], abc[SEC.second]);
						p[MAX.second]--;
						p[SEC.second]--;
					}
				} else {
					printf(" %c%c", abc[MAX.second], abc[SEC.second]);
					p[MAX.second]--;
					p[SEC.second]--;
				}
			}
		}
		printf("\n");
	}
	return 0;
}