#include <string>
#include <stdio.h>
#include <iostream>

using namespace std;

int main() {
	int t;
	scanf("%d", &t);

	int n, up, numFriends;

	for(int i = 1; i <= t; ++i) {
		scanf("%d ", &n);

		string shyness;
		cin >> shyness;

		numFriends = 0;
		up = shyness[0] - '0';

		for(int j = 1; j <= n; ++j) {
			if(j > up) {
				numFriends += j - up;
				up = j;
			} 

			up += shyness[j] - '0';
		}


		printf("Case #%d: %d\n", i, numFriends);
	}
}