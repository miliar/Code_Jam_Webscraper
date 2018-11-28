#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>

using namespace std;

const char* filename = "B-large.in";

struct TestCase {
	double c;
	double f;
	double x;
};

struct TestCases {
	TestCase* c;
	TestCases* next;
};

TestCases* readTestCases(int &numCases) {
	ifstream fin;
	fin.open(filename);

	if(!fin.is_open()) {
		cout<<"input file not opened!"<<endl;
		return nullptr;
	}
	TestCases* cases = new TestCases();
	TestCases* curCase = cases;

	fin>>numCases;

	for(int i=0;i<numCases;i++) {
		curCase->next = new TestCases();
		curCase = curCase->next;
		curCase->c = new TestCase();
		TestCase* c = curCase->c;
		fin>>c->c>>c->f>>c->x;
	}

	fin.close();
	curCase = cases->next;
	delete cases;
	return curCase;
}

void deleteTestCases(TestCases* cases) {
	TestCases* c = cases;
	while(cases != nullptr) {
		c = cases->next;
		delete cases;
		cases = c;
	}
}

double solveTestCase(TestCase* c) {
	double currentBest = 0.0f;
	double nextTime = 0.0f;
	int numFactories = 0;
	double factoryTime = 0.0f;
	bool found = false;
	

	while(!found) {
		nextTime = c->x / (2.0f + numFactories * c->f) + factoryTime;
		factoryTime += c->c / (2.0f + numFactories++ * c->f);

		if(currentBest > 0.0f && nextTime > currentBest) {
			found = true;
		} else {
			currentBest = nextTime;
		}
	}

	return currentBest;
}

int main() {
	int numCases = 0;
	TestCases* cases = readTestCases(numCases);

	ofstream fout;
	fout.open("output.txt");

	if(!fout.is_open()) {
		cout<<"output file not opened!"<<endl;
		return -1;
	}

	TestCases* cur = cases;
	fout<< fixed << setprecision(7);
	for(int i=1;i<=numCases;i++) {
		fout<<"Case #"<<i<<": "<<solveTestCase(cur->c)<<endl;
		cur = cur->next;
	}


	fout.close();

	deleteTestCases(cases);
	cases = nullptr;

	return 0;
}