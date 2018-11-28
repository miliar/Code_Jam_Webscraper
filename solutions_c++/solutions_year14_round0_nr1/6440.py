#include <iostream>
#include <fstream>
using namespace std;

int Card[17] = {0,};

int main() {
	int N, T, Temp, RESULT, RESULT_KEY;
	ifstream fin;
	ofstream fout;
	
	fin.open("A-small-attempt1.in");
	fout.open("A-small-answer1.in");

	fin >> N;
	for(int mcase=1;mcase<=N;mcase++) {
		for(int i=1;i<=16;i++) Card[i] = 0;

		for(int k=1;k<=2;k++) {
			fin >> T;
			for(int i=1;i<=16;i++) {
				fin >> Temp;
				if((((i-1)/4)+1) == T) Card[Temp]++;
			}
		}

		RESULT = 0;
		for(int i=1;i<=16;i++) {
			if(Card[i] >= 2) {
				RESULT_KEY = i;
				RESULT++;
			}
		}
		fout << "Case #" << mcase << ": ";
		if(RESULT > 1) {
			fout << "Bad magician!";
		} else if(RESULT == 1) {
			fout << RESULT_KEY;
		} else {
			fout << "Volunteer cheated!";
		}
		fout << endl;
	}
	fout.close();
	return 0;
}