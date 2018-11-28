#include <iostream>
#include <string>
#include <stdlib.h>
using namespace std;
int main() {
	int numcases;
	cin >> numcases;
	int audience[1000];
	char temp[1001];
	for (int i = 0; i < numcases; i++) {
		int maxShy;
		cin >> maxShy >> temp;
		for (int j = 0; j < maxShy + 1; j++) {
			audience[j] = temp[j] - '0';
		}
		int numFriends = 0;
		int numStanding = 0;
		for (int j = 0; j < maxShy + 1; j++) {
			if (numStanding < j) {
				numFriends++;
				numStanding++;
			}
			numStanding += audience[j];
			if (numStanding >= maxShy) {
				break;
			}	
		}
		cout << "Case #" << i + 1 << ": " << numFriends << endl;
	}
	return 0;
}
