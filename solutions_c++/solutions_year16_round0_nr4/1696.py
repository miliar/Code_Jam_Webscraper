#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>
#include <string>
#include <sstream>
#include <cmath>
using namespace std;

int main () {
	freopen("d.in", "r", stdin);
	freopen("d.out", "w", stdout);

	int T, K, C, S;
	cin >> T;
	
	for (int i = 1; i <= T; i++) {
		cin >> K >> C >> S;
		cout << "Case #" << i << ":";
		for (int j = 1; j <= K; j++) {
			cout << " " << j;
		}
		cout << endl;
	}
	return 0;
}
