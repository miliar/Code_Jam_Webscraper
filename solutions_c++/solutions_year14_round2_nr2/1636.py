#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int j = 1; j <= t; j++) {
		int A, B, K, cost = 0;
		cin >> A >> B >> K;
		for (int i = 0; i <= A - 1; i++) {
			for (int k = 0; k <= B - 1; k++) {
				if ((i & k) < K) {
					cost++;
				}
			}
		}
		cout << "Case #" << j << ": " << cost << endl;
	}

}
