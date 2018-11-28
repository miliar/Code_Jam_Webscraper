#include <iostream>
#include <fstream>
#include <algorithm>
#include <limits.h>
#include <vector>

using namespace std;

ofstream output;
int contFilePos = 0;

int nextInteger (char * buffer) {

	int number = 0;
	bool togle_negative = false;
	char c = buffer[contFilePos++];

	if (c == '-') {
		togle_negative = true;
		c = buffer[contFilePos++];
	}

	while ((c >= '0') && (c <= '9')) {

		number = number * 10 + c - '0';
		c = buffer[contFilePos++];
	}

	if (togle_negative) {
		number *= -1;
	}

	return number;
}

int main () {

	const string BAD_MAGICIAN = "Bad magician!";
	const string CHEAT = "Volunteer cheated!";

	FILE * pFile;
	long lSize;
	char * buffer;
	pFile = fopen ( "input.txt" , "r" );
	fseek (pFile , 0 , SEEK_END);
	lSize = ftell (pFile);
	rewind (pFile);
	buffer = (char*) malloc (sizeof(char)*lSize);
	fread (buffer,1,lSize,pFile);

	output.open("output.txt", fstream::trunc);

	int lenght = nextInteger(buffer);

	// Analizza i vari casi
	for (int i = 0; i < lenght; i++) {

		int retry1[4][4];
		int retry2[4][4];

		int answer1 = 0;
		int answer2 = 0;

		cout<<"Case #"<<i+1<<endl;

		// Leggi riposta 1
		answer1 = nextInteger(buffer) -1;
		cout<<"Answer 1: "<<answer1<<endl;

		// Leggi disposizione carte 1
		for (int y = 0; y < 4; y++) {
			for (int x = 0; x < 4; x++) {
				retry1[y][x] = nextInteger(buffer);

				cout<<retry1[y][x]<<" ";
			}
			cout<<endl;
		}

		// Leggi riposta 2
		answer2 = nextInteger(buffer) -1;
		cout<<"Answer 2: "<<answer2<<endl;

		// Leggi disposizione carte 2
		for (int y = 0; y < 4; y++) {
			for (int x = 0; x < 4; x++) {
				retry2[y][x] = nextInteger(buffer);
				cout<<retry2[y][x]<<" ";
			}
			cout<<endl;
		}

		// Salva possibili carte
		vector<int> solution;

		bool check = false;

		for (int y = 0; y < 4; y++) {
			for (int x = 0; x < 4; x++) {

				if (retry1[answer1][y] == retry2[answer2][x]) {

					cout<<"Found a card: "<<retry1[answer1][y]<<endl;
					solution.push_back(retry1[answer1][y]);

					if (solution.size() > 1) {
						cout<<"But there is alredy one!"<<endl;
						check = true;
						break;
					}
				}
			}

			if (check) {
				break;
			}
		}

		// Analizza stato del trucco
		if (solution.size() == 0) {
			output<<"Case #"<<i+1<<": "<<CHEAT<<endl;
			cout<<"Cards found: "<<solution.size()<<endl<<CHEAT<<endl;
		}
		else if (solution.size() == 1) {
			output<<"Case #"<<i+1<<": "<<solution[0]<<endl;
			cout<<"Cards found: "<<solution.size()<<endl<<">>>The solution is: "<<solution[0]<<endl;
		}
		else if (solution.size() > 1) {
			output<<"Case #"<<i+1<<": "<<BAD_MAGICIAN<<endl;
			cout<<"Cards found: "<<solution.size()<<endl<<BAD_MAGICIAN<<endl;
		}
	}

	output.close();
}

