#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;


int main(int argc, char* argv[]){
	int T;
	vector<int> input(1000); // D <= 1000

	ifstream ifs("B-large.in", ifstream::in);
	ofstream ofs("B-large.out");
	
	ifs >> T; //  # test cases
	for(int it = 0; it<T; it++)
	{
		// input
		input.clear();
		int D = 0;
		ifs >> D;
		int Pi;
		int maxp=0;
		for(int i = 0; i < D; i++){
			ifs >> Pi;
			input.push_back(Pi);
			maxp = max(maxp, Pi);
		}

		// compute
		int minutes = maxp;
		for(int p = 2; p <= maxp; p++){ // p is the largest # in each plate for optimal solution
			int temp = p;
			for(int i = 0; i < D; i++){
				if(input[i]%p == 0)
					temp += input[i]/p - 1;
				else
					temp += input[i]/p;
			}
			minutes = min(minutes, temp);
		}

		// output
		ofs << "Case #" << it+1 << ": " << minutes << endl;
	}
	ifs.close();
	ofs.close();
	return 0;
}