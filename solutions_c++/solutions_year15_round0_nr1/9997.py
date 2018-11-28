#include <iostream>
#include <string>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int main () {

	int testCases;
	cin >> testCases;

	for ( int j = 0; j < testCases; j++ ) {
		//retrieve input
		string sMax;
		string input; 
		cin >> sMax;
		cin >> input;

		//initialize vars
		int standing = 0;
		int invited = 0;
		int currentNumber = 0;
		int size = atoi(sMax.c_str());

                //iterate through array
                //current index is the required amount of ppl needed to be standing to proceed
                //if index-standing > 0 
                //     this means additional ppl are required to stand before proceeding
                //     invite the difference of ppl
                //     add the invited ppl to current pool of ppl standing
                //     add the ppl of this shyness level to the current pool of ppl standing
                //else
                //     just add the ppl of this shyness level to the current pool of ppl standing
                //
		for ( int i = 0; i < size+1 ; i++ ) {
			currentNumber = input[i] - '0'; 
			if ( ( i-standing ) > 0 && ( currentNumber != 0) ) {
				invited += i-standing;
				standing += invited;
			}
			standing += currentNumber;
		}
		cout << "Case #" << j+1 << ": " << invited << endl;
	}
}
