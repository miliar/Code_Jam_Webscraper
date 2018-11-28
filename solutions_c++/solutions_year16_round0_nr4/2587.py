#include <iostream>
#include <stdio.h>
#include <memory.h>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	cin >> T;
	for (int caseID = 1; caseID <= T; ++caseID) {
		int K, C, S;
		cin >> K >> C >> S;
		printf("Case #%d:", caseID);
		for (int i = 1; i <= S; ++i) {
			cout << " " << i;
		}
		cout << endl;
	}
}