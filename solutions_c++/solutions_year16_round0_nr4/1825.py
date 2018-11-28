#include <cassert>
#include <fstream>
#include <iostream>
#include <memory>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

string solve(string& input)
{
	stringstream ssin(input);
	stringstream ssout;
	int K, C, S;
	ssin >> K >> C >> S;
	assert(S == K);
	for (int k = 0; k < K; ++k) {
		ssout << " " << k + 1;
	}
	return ssout.str();
}

int main(int argc, char *argv[])
{
	unique_ptr<ifstream> in_p;
	if (argc > 1) {
		in_p.reset(new ifstream(argv[1]));
		cin.rdbuf(in_p->rdbuf());
	}
	int numCases;
	cin >> numCases;
	cin.ignore();
	vector<string> input(numCases);
	vector<string> output(numCases);
	for (int i = 0; i < numCases; ++i) {
		getline(cin, input[i]);
	}
	#pragma omp parallel for
	for (int i = 0; i < numCases; ++i) {
		output[i] = solve(input[i]);
	}
	for (int i = 0; i < numCases; ++i) {
		cout << "Case #" << i + 1 << ":" << output[i] << endl;
	}
}
