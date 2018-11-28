#include <iostream>
#include <cstdio>

using namespace std;

int main() {
	int T; cin >> T;
	
	for (int t = 1; t <= T; t++) {
		double C, F, X;
		cin >> C >> F >> X;
		double pre;
		double costoFattorie = 0;
		double ratio = 2;		
		double curr = 10000000000.0;
		do {
			pre = curr;
			curr = costoFattorie + X / ratio;
			costoFattorie += C / ratio;
			ratio += F;			
		} while (pre > curr);
		printf("Case #%d: %.7f\n", t, pre);
	}	
}
