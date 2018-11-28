#include <string>
#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

long int solveA(vector<int> &M){
	long int sum = 0;
	for(unsigned i=0; i<M.size()-1; i++){
		if(M[i] > M[i+1]){
			sum += (M[i] - M[i+1]);
		}
	}
	return sum;
}

long int solveB(vector<int> &M){
	long int grosstes_delta = 0;
	for(unsigned i=0; i<M.size()-1; i++){
		if(M[i] - M[i+1] > grosstes_delta)
			grosstes_delta = M[i] - M[i+1];
	}
	
	long int sum = 0;
	for(unsigned i=0; i<M.size()-1; i++){
		if(M[i] < grosstes_delta)
			sum += M[i];
		else
			sum += grosstes_delta;
	}

	return sum;
}



int main (int argn, char** args){
	std::string in = args[1];
	std::string out = args[2];

	std::fstream input(in, std::ios_base::in);
	std::fstream output(out, std::ios_base::out);
	
	unsigned int cases;
	input >> cases;
	for(unsigned i=0; i<cases; i++){
		unsigned int N;
		input >> N;
		
		vector<int> M = vector<int>(N);
		for(unsigned i=0; i<N; i++)
			input >> M[i];
		
		output << "Case #" << (i+1) << ": " << solveA(M) << " " << solveB(M) << "\n";
	}


	return 0;
}