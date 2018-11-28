#include <iostream>
#include <fstream>
using namespace std;
int main() {
	long long int T, P, Q;
	char temp;
	ifstream fin;
	ofstream fout;
	
	fin.open("B-large.in");
	fout.open("B-large-answer.in");
	fin >> T;
	for(int mcase=1;mcase<=T;mcase++) {
		fout << "Case #" << mcase << ": ";

		fin >> P >> temp >> Q;
		long long int generation = 1, temp = 0;
		while(1) {
			if(Q%2 == 0) {
				Q /= 2;
				if(Q <= P) { // 현재 세대 조상에 1/1 Elf가 있다. 
					if(P == Q) {
						break;
					} else {
						temp = 1;
						P -= Q;
					}
				}
				if(temp == 0) generation++;
			} else {
				generation = -1;
				break;
			}
		}
		if(generation == -1) fout << "impossible";
		else fout << generation;
		fout << endl;
	}
	fout.close();
	return 0;
}