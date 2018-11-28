#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void parseK(int size, int kvalues[], string kstring) {
	for (int i = 0; i < size; i++) {
		kvalues[i] = kstring.at(i) - '0';
	}
}

int main() {
	ifstream data("A-large.in");
	ofstream outfile("A-largeout.txt");

	int cases;
	data >> cases;

	for (int i = 0; i < cases; i++) {
		int smax;
		string kstring;

		data >> smax;
		data >> kstring;

		int kvalues[smax+1] ;
		parseK(smax+1, kvalues, kstring);

		int clapping = 0;
		int need = 0;

		for (int j = 0; j < smax+1; j++) {
			clapping += kvalues[j];
			if (j+1 > clapping) {
				int dif = j+1-clapping;
				need += dif;
				clapping += dif;
			}
		}

		outfile << "Case #" << i+1 << ": " << need << endl;
	}
	outfile.close();

}
