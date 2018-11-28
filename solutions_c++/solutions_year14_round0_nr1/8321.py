// Requires C++ 0x // C++11 support in compiler
#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;

int main(void) {
	int T;
	cin >> T;
	uint16_t mask;

	for(int t=1; t<=T; ++t) {
		mask = 0;
		int r1;
		cin >> r1;
		for(int i=1; i<=4; ++i) {
			for(int j=0; j<4; ++j) {
				int v;
				cin >> v;
				if(r1 == i)
					mask |= 1<<(v-1);
			}
		}
		int r2;
		cin >> r2;
		bool found = false;
		bool bad = false;
		int ans=0;
		for(int i=1; i<=4; ++i) {
			for(int j=0; j<4; ++j) {
				int v;
				cin >> v;
				if(r2 == i) {
					if( mask & 1<<(v-1)) {
						if(found) {
							bad = true;
						} else {
							found = true;
							ans = v;
						}
					}
				}
			}
		}
		cout << "Case #" << t <<": ";
		if(bad) {
			cout << "Bad magician!";
		} else if(found) {
			cout << ans;
		} else {
			cout << "Volunteer cheated!";
		}
		cout << endl;
	}
}
