//program sudoku checker
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
//#include <math.h>
//#include <list>
#include <algorithm>
#include <tokenizer.hpp>  //split function to tokenize strings according to delimiters
//#include <Array2D.hpp> //simple multi-array implementation

using namespace std;


//this method solves the problem
string solve(vector<string> lines, int size) {
	string solution = "";
	vector<string> aux;
	int count = 0;
	aux = split(lines[0]);
	int A = stoi(aux[0]);
	int B = stoi(aux[1]);
	int K = stoi(aux[2]);

	for (register int i = 0; i < A; ++i) {
		for (register int j = 0; j < B; ++j) {
			if ((i&j) < K) ++count;
		}
	}
	stringstream ss(solution);
	ss << count;
	ss >> solution;

	return solution;
}

int main(int argc, char* argv[]) {
	string in, temp, line;
	if (argc<2 || argc>3) {
		cout << "Please use <app> <infile> <outfile>" << '\n';
		return 0;
	}
	in = argv[1];
	string out = (argc == 3) ? argv[2] : "out.txt";
	
	//reading input file
	ifstream myfile(in);
	ofstream myoutfile(out);
	if (myfile.is_open()&&myoutfile.is_open())
	{
		//read first line, with number of problems to solve
		getline(myfile, line);
		int times = stoi(line); //number of use cases
		int count = 0;
		//solve X problems
		while (count<times) {
			getline(myfile, line);
			int n = 1;
			//int n = stoi(line);
			vector<string> entry;
			//int rows = n;
			//for (int i = 0; i < rows; ++i) {
			//	getline(myfile, line);
				entry.push_back(line);
			//}
			//work with the input file one line each time
			myoutfile << "Case #" << (++count) << ": " << solve(entry,n) << '\n';
			//cout << line << '\n';
		}
		myfile.close();
		myoutfile.close();
	}
	else cout << "Unable to open file\n";
	return 0;
}