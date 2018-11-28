#include <cstdio>
#include <cstdlib>
#include <iostream>
using namespace std;

int main() {

	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);

	int cases;
	cin >> cases;

	for (int c = 1; c <= cases; c++) {
		int K, C, S;
		cin >> K >> C >> S;
		
		cout << "Case #" << c << ":";
		for (int i = 1; i <= K; i++) {
			cout << " " << i;
		}
		cout << endl;
		

	}


	return 0;
}