#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;

//#define DEBUG 

int main (int argc, char** argv) {

	int testCases;

	cin >> testCases;

	for (int test = 0; test < testCases; ++test) {

		int sMax;

		cin >> sMax;

		int friends = 0;
		int clapping = 0;

		string histogram;
		cin >> histogram;

		for (int i = 0; i < sMax + 1; ++i) {

			int sI = histogram[i] - '0';

			if (clapping < i) {
				++friends;
				++clapping;
			}

			clapping += sI;
		
		}
		
		cout << "Case #" << test + 1 << ": " << friends << endl;

	}

	return 0;
}
