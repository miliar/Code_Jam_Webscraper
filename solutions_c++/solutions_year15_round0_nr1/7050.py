#include <iostream>
#include <fstream>
#include <stdlib.h>

using namespace std;

int main(int argc, char* argv[]) {
	ofstream os("out.txt");
	ifstream is("A-large.in");
	int numTestCases;
	is >> numTestCases;
	for(int i = 1; i <= numTestCases; ++i) {
		os << "Case #" << i << ": ";
		int peopleNeeded = 0;
		int maxShyness;
		is >> maxShyness;
		int audience[maxShyness+1];
		is.get(); //burn the space before the audience string
		for(int j = 0; j <= maxShyness; ++j)
			audience[j] = is.get() - 48; //convert ASCII -> int
		//excess tracks the number of people we don't need to bring,
		//because an audience member will stand in their place
		int excess = 0;
		for(int j = 0; j <= maxShyness; ++j) {
			excess += audience[j];
			if(excess == 0) {
				++excess;
				++peopleNeeded;
			}
			--excess;
		}
		os << peopleNeeded << endl;
	}
}