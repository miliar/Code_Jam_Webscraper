#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>
#include <vector>
#include <sstream>
#include <cmath>
#include <bitset>
#include <iomanip>
#include <list>
#include <algorithm>

using namespace std; // contest use

using Solver_Tpf = void (*)(int, ifstream&);

list<long> dividers(long val, int n = 1)
{
	list<long> allDividers;
	for(long i = 2 ; i <= sqrt(val) && allDividers.size() < n ; ++i) {
		if ( val % i == 0 ) {
			allDividers.push_front(i);
		}
	}

	return allDividers;
}

void solve_case(int index, ifstream& stream)
{
	string line;
	getline(stream, line);
	istringstream input(line);
	getline(input, line, ' ');
	int length = stoi(line);
	getline(input, line);
	int count = stoi(line);
	int realLength = length - 2;
	vector<string> potential;
	potential.reserve(pow(2.0, realLength));

	string maxBin(realLength, '1');

	long jamFoundCount = 0;
	ostringstream totalOutput;

	for(int i = 0 ; i <= stoi(maxBin, nullptr, 2) && jamFoundCount < count ; ++i) {
		ostringstream o;
		o << bitset<32>(i);
		auto num = o.str();
		auto current = num.substr(num.length() - realLength);
		current.insert(0, "1");
		current += "1";

		bool isPrime = false;
		ostringstream output;

		for(int b = 2 ; b <= 10 && !isPrime ; ++b) {
			long valInBase = stol(current, nullptr, b);
			auto allDividers = dividers(valInBase);
			if ( allDividers.size() == 0 ) {
				isPrime = true;
			}
			else {
				output << allDividers.front() <<  " ";
			}
		}

		if ( !isPrime ) {
			auto result = output.str();
			totalOutput << current << " " << result.substr(0, result.size() - 1) << endl;
			++jamFoundCount;
		}
	}

	if (!totalOutput.str().empty()) {
		cout << "Case #" << index << ": " << endl << totalOutput.str();
	}
}

void read(ifstream& stream, Solver_Tpf solver)
{
	string line;
	getline(stream, line);
	int casesCount = stoi(line);
	for(int index = 1 ; index <= casesCount ; ++index) {
		solver(index, stream);		
	}
}

int main(int argc, char** argv)
{
	using namespace std;

	if ( argc <= 1 ) {
		return EXIT_FAILURE;
	}

	const char* filename = argv[1];
	ifstream input(filename);
	Solver_Tpf solver = &solve_case;

	if ( input ) {
		read(input, solver);
		input.close();
	}
}
