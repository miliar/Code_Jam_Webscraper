#include <cstdlib>
#include <fstream>
#include <iostream>
#include <vector>
#include <queue>
#include <cmath>

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

class Elem
{
public:
	Elem(int arg_taskIdx, int arg_value) : taskIdx(arg_taskIdx), value(arg_value) { };
	bool operator<(const class Elem e) const { return value < e.value; }
	int taskIdx;
	int value;
};

void processCase(istream& inputFile, ostream& outputFile)
{
	long int maxEn, regen;
	int numActs;
	inputFile >> maxEn >> regen >> numActs;
	vector<long int> values(numActs);
	priority_queue<Elem> pq;
	for (int i=0; i<numActs; i++) {
		inputFile >> values[i];
		pq.push(Elem(i, values[i]));
	}
	vector<long int> enBefore(numActs, maxEn), enUsed(numActs, 0), enNeeded(numActs, 0);
	unsigned long int result = 0;
	while (!pq.empty()) {
		int actIdx = pq.top().taskIdx;
//		cout << result << "  now maxing task " << actIdx << " with value " << pq.top().value << "\n";
		if (actIdx == numActs-1) {
			enUsed[actIdx] = enBefore[actIdx];
			enNeeded[actIdx] = max(enUsed[actIdx] - regen, 0L);
		} else {
			enUsed[actIdx] = enBefore[actIdx] - enNeeded[actIdx+1];
			enNeeded[actIdx] = max(enUsed[actIdx] + enNeeded[actIdx+1] - regen, 0L);
		}
//		cout << "using " << enUsed[actIdx] << "\n";
		result += enUsed[actIdx] * values[actIdx];
		for (int i=actIdx+1; i<numActs; i++)
			enBefore[i] = min(enBefore[i-1] - enUsed[i-1] + regen, maxEn);
		for (int i=actIdx-1; i>=0; i--)
			enNeeded[i] = max(enUsed[i] + enNeeded[i+1] - regen, 0L);
		pq.pop();
//		cout << "enBefore: "; for (int i=0;i<numActs;i++) cout << enBefore[i] << " "; cout << "\n";
//		cout << "enUsed:   "; for (int i=0;i<numActs;i++) cout << enUsed[i] << " "; cout << "\n";
//		cout << "enNeeded: "; for (int i=0;i<numActs;i++) cout << enNeeded[i] << " "; cout << "\n";
	}
	outputFile << result;
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


