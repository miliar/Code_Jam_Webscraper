#include <stdio.h>
#include <fstream>
#include <string>
using namespace std;

int getStep(string cakes, int k){

	int n = cakes.length();

	int cnt = 0;
	for (int i = 0; i < n; ++i){
		if (cakes[i] == '-'){
			if (i + k <= n){
				for (int j = i; j < i + k; ++j){
					cakes[j] = (cakes[j] == '-')?'+':'-';
				}
				cnt++;
			}
			else{
				return -1;
			}
		}
	}

	return cnt;
}

int main(int argc, char** args){

	ifstream in_file ("input.txt");
	ofstream out_file("output.txt");

	int T;
	in_file >> T;
	string cakes;
	int k;
	for (int t = 0; t < T; ++t){
		in_file >> cakes >> k;
		int rst = getStep(cakes, k);

		out_file << "Case #" << t + 1 << ": ";
		if (rst >= 0){
			out_file << rst << std::endl;
		}
		else{
			out_file << "IMPOSSIBLE" << std::endl;
		}
	}

	return 0;
}