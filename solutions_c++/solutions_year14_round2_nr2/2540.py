#include <iostream>
#include <fstream>

using namespace std;


void main(){

	fstream fin, fout;

	fin.open("input.in", ios::binary | ios::in);
	fout.open("out.txt", ios::trunc | ios::out);

	unsigned long long int T, A, B, K;

	fin >> T;

	unsigned long long int count = 0;

	for (unsigned long long int x = 1; x <= T; x++){
	
		fin >> A >> B >> K;

		count = 0;

		for (unsigned long long int i = 0; i < A; i++){
		
			for (unsigned long long int j = 0; j < B; j++){
			
				if ((i & j) < K)
					count++;

			}

		}

		fout << "Case #" << x << ": " << count << endl;

	}


}