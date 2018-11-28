#include <cstdio>
#include <iostream>
using namespace std;

int main(void) {
	int T;
	cin >> T;
	char digit;
	int S[10000], S_max, friendsAdded, standing, toAdd;
	for (int t=1; t<=T; t++) {
		cin >> S_max;
		for (int i=0; i<=S_max; i++) {
			cin >> digit;
			S[i] = digit - '0';
		}
		
		friendsAdded = 0;
		standing = S[0];
		for (int i=1; i<=S_max; i++) {
			if (S[i]) {
				if (standing < i) {
					toAdd = i - standing;
					friendsAdded += toAdd;
					standing += toAdd;
				}
				standing += S[i];
			}
		}
		printf("Case #%d: %d\n", t, friendsAdded);
	}
	return 0;
}