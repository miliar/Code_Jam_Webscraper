#include <iostream>
#include <fstream>

using namespace std;

int getFriends(int smax, int levels[]) {
	int currentSum = 0;
	int friends = 0;
	int k = 0;
	bool repeat = false;
	while(k < smax || repeat) {
		if(!repeat) {
			currentSum += levels[k];
		}
		if(currentSum - (k+1) >= 0 || levels[k+1] == 0) {
			k++;
			repeat = false;
		}
		else {
			friends++;
			currentSum ++;
			repeat = true;
		}
	}

	return friends;
}

int main() {
	ifstream fin;
	fin.open("A-large.in");
	int smax = 0;
	int string = 0;
	ofstream fout;
	fout.open("output-large.txt");
	int T = 0;
	fin >> T;
	char tempChar;
	for(int i = 1; i <= T; i++) {
		fin >> smax;
		int* tempArray = new int[smax+1];
		for(int j = 0; j < smax+1; j++) {
			fin >> tempChar;
			tempArray[j] = tempChar-48;
		}
		fout << "Case #" << i << ": " << getFriends(smax, tempArray) << endl;
	}


	return 0;
}