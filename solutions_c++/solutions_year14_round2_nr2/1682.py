#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
using namespace std;

int main(){
	ifstream fin;
	ofstream fout;
	int T;

	fin.open("input.txt");
	fout.open("output.txt");
	fin >> T;

	for (int k = 1; k <= T; k++){
		unsigned long s = 0;
		unsigned long A, B, K;
		fin >> A >> B >> K;
		for (unsigned long i = 0; i < A; i++){
			for (unsigned long j = 0; j < B; j++){
				unsigned long c = i & j;
				if (c < K){
					s++;
				}
			}
		}

		fout << "Case #" << k << ": " << s << endl;
	}
	fin.close();
	fout.close();
}