#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>
#include <vector>
#include <map>
#include <sstream>
#include <algorithm>

using namespace std; // contest use

using Solver_Tpf = void (*)(int, ifstream&);

void solve_case(int index, ifstream& stream)
{
	string line;
	getline(stream, line);
	int startingNumber = stoi(line);

	if ( startingNumber == 0 ) {
		cout << "Case #" << index << ": INSOMNIA" << endl;
		return;
	}

	bool allDigitsSeen = false;
	int lastNumber = startingNumber;
	map<char, int> digitsSeen = {{'0', 0}, {'1', 0}, {'2', 0},
		{'3', 0}, {'4', 0}, {'5', 0}, {'6', 0}, {'7', 0}, {'8', 0},
		{'9', 0}};

	for(int i = 1 ; !allDigitsSeen ; ++i) {
		stringstream out;
		out << (i * startingNumber);
		line = out.str();
		lastNumber = stoi(line);
		for_each(line.begin(), line.end(), [&digitsSeen](char c) {
					digitsSeen[c]++;
				});

		allDigitsSeen = true;
		for(auto digitCount : digitsSeen) {
			if ( digitCount.second == 0 ) {
				allDigitsSeen = false;
			}
		}
	}

	cout << "Case #" << index << ": " << lastNumber << endl;
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
