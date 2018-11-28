#include <cstdlib>
#include <fstream>
#include <iostream>
#include <vector>
#include <cmath>
#include <cassert>
#include <set>

using namespace std;

void getInputFile(int argc, char* argv[], ifstream &inputFile)
{
	if (argc != 2) {
		cerr << "Require one argument (input file); exiting ...\n";
		exit(1);
	}
	string filename = argv[1];
	inputFile.exceptions(ifstream::failbit);
	inputFile.open(filename.c_str());
}

void getOutputFile(int argc, char* argv[], ofstream &outputFile)
{
	string filename = argv[1];
	unsigned dotIndex = filename.find_last_of('.');
	if (dotIndex != string::npos)
		filename.erase(dotIndex);
	filename += ".out";
	outputFile.exceptions(ofstream::failbit);
	outputFile.open(filename.c_str());
}

void processCase(istream& inputFile, ostream& outputFile)
{
	outputFile << "\n";
	int numLines, numSels, maxNum, numProds;
	inputFile >> numLines >> numSels >> maxNum >> numProds;
	int numCombs = pow(maxNum-1, numSels);
	int numSubsets = pow(2, numSels);
	vector<vector<int> > numbers(numCombs);
	vector<set<int> > products(numCombs);
	for (int i=0; i < numCombs; i++) {
		// have things double: e.g. 2,2,3 or 2,3,2 or 3,2,2
		numbers[i].assign(numSels, 0);
		for (int j=0; j < numSels; j++) {
			numbers[i][j] = (i / int(pow(maxNum-1,j))) % (maxNum-1) + 2;
//			cout << numbers[i][j] << " ";
		}
//		cout << "\n   ";
		products[i].clear();
		for (int k=0; k < numSubsets; k++) {
			int product = 1;
			for (int j=0; j < numSels; j++) {
				if ((k / int(pow(2,j))) % 2 == 1)
					product *= numbers[i][j];
				products[i].insert(product);
//				cout << products[i][k] << " ";
			}
		}
//		cout << "\n";
	}

	vector<int> inputs(numProds);
	for (int n=0; n <  numLines; n++) {
		for (int k=0; k < numProds; k++)
			inputFile >> inputs[k];
		bool found = false;
		int i=0;
		while (!found) {
			assert(i <= numCombs);
			found = true;
			for (int k=0; k < numProds; k++)
				if (products[i].find(inputs[k]) == products[i].end())
					found = false;
			if (found) {
				for (int k=0; k < numSels; k++)
					outputFile << numbers[i][k];
				outputFile << "\n";
			}
			i++;
		}
	}
}

int main(int argc, char *argv[])
{
	ifstream inputFile;
	getInputFile(argc, argv, inputFile);
	ofstream outputFile;
	getOutputFile(argc, argv, outputFile);

	int numCases;
	inputFile >> numCases >> ws;
	for (int caseIndex = 0; caseIndex < numCases; ++caseIndex) {
		outputFile << "Case #" << caseIndex+1 << ": ";
		cout << "Case #" << caseIndex+1 << "\n";
		processCase(inputFile, outputFile);
		outputFile << "\n";
	}
}


