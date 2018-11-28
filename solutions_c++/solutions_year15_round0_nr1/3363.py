#include <iostream>
#include <stdio.h>
#include <string>
#include <math.h>

int whatis(char num){
	if (num == '0') {	return 0;	}
	if (num == '1') {	return 1;	}
	if (num == '2') {	return 2;	}
	if (num == '3') {	return 3;	}
	if (num == '4') {	return 4;	}
	if (num == '5') {	return 5;	}
	if (num == '6') {	return 6;	}
	if (num == '7') {	return 7;	}
	if (num == '8') {	return 8;	}
	if (num == '9') {	return 9;	}
};

using namespace std;

int main (int argc, char * const argv[]) {
    // insert code here...
    int cases, run, seat, before;
	cin >> cases;
	
	int smax, nfriends;
	string audience;
	int people[1001];
	
	for (run = 0; run < cases; run++) {
		seat = 0;
		before = 0;
		nfriends = 0;
		cin >> smax;
		cin >> audience;
		while (seat < smax + 1) {
			if (seat != 0 && nfriends < seat - before) {
				nfriends = seat - before;
			}
			before = before + whatis(audience[seat]);
			seat++;			
		}
		cout << "Case #" << run + 1 << ": " << nfriends << endl;
	}
	return 0;
}
