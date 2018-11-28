#include <iostream>
#include <math.h>

using namespace std;


int main() {
	
	int T, N;

	cin >> T;

	for(int i = 0; i < T; i++) {

		cin >> N;

		if(N == 0) {
			cout << "Case #" << (i+1) << ": INSOMNIA" << endl;
			continue;
		}

		bool digitsFound[10];
		int digitCounter = 0;

		for(int j = 0; j < 10; j++) {
			digitsFound[j] = false;
		}

		int cycleCounter = 1;

		while(true) {

			int temp = N * cycleCounter;

			while(temp > 0) {

				int temp2 = temp % 10;
				if(!digitsFound[temp2]) {
					digitsFound[temp2] = true;
					digitCounter++;
				}

				temp = floor(temp / 10);

			}

			if(digitCounter == 10) {
				cout << "Case #" << (i+1) << ": " << N*cycleCounter << endl;
				break;
			}

			cycleCounter++;

		}

	}

}