#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstdlib>
#include <cmath>
#include <iomanip>

using namespace std;

int main(){
	ifstream fin;
	ofstream fout;
	fin.open("input.in");
	fout.open("result.txt");
	int times;

	fin >> times;

	for (int i = 0; i < times; i++){
		int A, B, K;
		fin >> A;
		fin >> B;
		fin >> K;
		int time = 0;
		for (int i = 0; i < A; i++){
			for (int j = 0; j < B; j++){
				int C;
				C = i&j;
				if (C < K){
					time++;
				}
			}
		}
		fout << "Case #" << i + 1 << ": " << time << endl;
	}

	fin.close();
	fout.close();
	return 0;
}