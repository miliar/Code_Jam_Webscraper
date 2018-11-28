#include <iostream>
#include <fstream>
#include <string>

using namespace std;

const char* filename = "A-small-attempt1.in";

struct TestCase {
	int ans1,ans2;
	int cards1[16];
	int cards2[16];
};

struct TestCases {
	TestCase* c;
	TestCases* next;
};

TestCases* readTestCases(int &numCases) {
	ifstream fin;
	fin.open(filename);

	if(!fin.is_open()) {
		cout<<"file not opened!"<<endl;
		return nullptr;
	}

	TestCases* cases = new TestCases();
	TestCases* curCase = cases;

	fin>>numCases;

	for(int i=0;i<numCases;i++) {
		curCase->next = new TestCases();
		curCase = curCase->next;
		curCase->c = new TestCase();
		TestCase* pCase = curCase->c;

		fin>>pCase->ans1;
		for(int a=0;a<16;a++) {
			fin>>pCase->cards1[a];
		}

		fin>>pCase->ans2;
		for(int a=0;a<16;a++) {
			fin>>pCase->cards2[a];
		}
	}

	fin.close();
	return cases->next;
}

string solveCase(TestCase* c) {
	int number = -1;
	bool multiple = false;

	for(int i=(c->ans1-1)*4;i<c->ans1*4;i++) {
		for(int j=(c->ans2-1)*4;j<c->ans2*4;j++) {
			if(c->cards1[i] == c->cards2[j]) {
				if(number == -1) {
					number = c->cards1[i];
				} else {
					multiple = true;
				}
			}
		}
	}

	if(number == -1) {
		return "Volunteer cheated!";
	} else  if(multiple != false) {
		return "Bad magician!";
	} else {
		return to_string(number);
	}
}


int main() {
	int numCases = 0;
	TestCases *pCases = readTestCases(numCases);

	cout<<"read "<<numCases<<" cases"<<endl;

	ofstream fout;
	fout.open("output.txt");

	if(!fout.is_open()) {
		cout<<"error writing output file!"<<endl;
		return -1;
	}

	for(int i=1;i<=numCases;i++) {
		fout<<"Case #"<<i<<": "<<solveCase(pCases->c)<<endl;
		pCases = pCases->next;
	}

	return 0;
}