#include <iostream>
#include <ios>
#include <fstream>
#include <string>
#include <sstream>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <set>
#include <vector>

using namespace std;

void goFirst(int limit, vector<int> &senatorVec, vector<int> &out) {
	int count = 0;
	for (int i = 0; i != senatorVec.size(); ++i)	{
		if (senatorVec[i] > 0 && count < limit) {
			--senatorVec[i];
			out.push_back(i);
			++count;
		}
	}
}

bool goTwo(int total, vector<int> &senatorVec, vector<int> &out) {
	total -= 2;
	int half = total / 2;
	for (int i = 0; i != senatorVec.size(); ++i) {
		while (senatorVec[i] > half){
			--senatorVec[i];
			out.push_back(i);
		}
	}

	if (out.size() > 2)	{
		for (int i = 0; i != out.size(); ++i) {
			++senatorVec[i];
		}
		out.clear();
		return false;
	}
	
	if (out.size() < 2) {
		goFirst(2 - out.size(), senatorVec, out);
	}
	return true;
}

string evacuate(int total, vector<int> &senatorVec) {
	stringstream senquence;
	while (total > 0) {
		vector<int> out;
		if (goTwo(total, senatorVec, out)){
			total -= 2;
		}
		else {
			total -= 1;
			goFirst(1, senatorVec, out);
		}

		for (int i = 0; i != out.size(); ++i) {
			senquence <<  (char) ('A' + out[i]);
		}
		senquence << " ";
	}
	return senquence.str();
}

int main(int argc, char *argv[])
{
	if (argc < 2) {
		cout << "Missing arguments!" << endl;
		return -1;
	}

	ifstream inputFile(argv[1]);
	string outputFileName = string(argv[1]) + ".out";
	ofstream outputFile(outputFileName.c_str(), ios::out | ios::trunc);
	if (!inputFile || !outputFile) {
		cout << "Open file error" << endl;
		return -2;
	}

	string line;
	getline(inputFile, line);
	int caseNum = atoi(line.c_str());
	int i = 0;
	while (i < caseNum) {
		int n;
		inputFile >> n;
		vector<int> senatorVec;
		int j = 0;
		int tmp = 0;
		int sum = 0;
		while (j++ < n)	{
			inputFile >> tmp;
			senatorVec.push_back(tmp);
			sum += tmp;
		}

		outputFile << "Case #" << ++i << ": " << evacuate(sum, senatorVec) << endl;

	}
	outputFile.flush();
	inputFile.close();
	outputFile.close();
	return 0;
}
