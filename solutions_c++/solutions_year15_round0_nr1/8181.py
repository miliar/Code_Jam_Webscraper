#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;

#define SMAX 1002
#define DBG 0
#define PIF(nr, tnr, command) \
	if (DBG) \
		do { \
			if (nr == tnr) \
				{ command; } \
		} while(0)


int s[SMAX];
int nStanding, smax, t, nFriends;
string crowd;

int main() {

	cin >> t;
	for (int _t=1; _t<=t; ++_t) {

		// Init variables
		nFriends = nStanding = 0;

		cin >> smax >> crowd;
		for (int i=0; i<crowd.size(); ++i) 
			s[i] = crowd[i]-'0';

		PIF(_t,0, printf("smax(%d) = %d\n", _t, smax));
		for (int i=0; i<=smax; ++i) {
			if (nStanding >= i)
				nStanding += s[i];
			else {
				nFriends += i-nStanding;
				nStanding += i-nStanding + s[i];
			}
			PIF(_t,2, printf("nStanding(%d) = %d\n", _t, nStanding));
		}	

		printf("Case #%d: %d\n", _t, nFriends);
	}
}