#include <fstream>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <windows.h>
#include <iomanip>

using namespace std;

void processCase(ifstream &infile, ofstream &outfile, int number);

int main() {
	ifstream infile;
	ofstream outfile;
	string filename = "D-large.in";
	string filename1 = "A-small-practice.out";
	infile.open(filename.c_str());
	outfile.open(filename1.c_str());
	int cases;
	infile >> cases;
	for (int i = 1; i <= cases; i++) {
		processCase(infile, outfile, i);
	}
	return 0;
}

int War(vector<double> Naomi, vector<double> Ken, int N) {
	int result = 0;
	for (int i = 0; i < N; i++) {
		if (Naomi[i] > Ken.back()) {
			result++;
			Ken.erase(Ken.begin());
		} else {
			for (int j = 0; j < Ken.size(); j++) {
				if (Ken[j] > Naomi[i]) {
					Ken.erase(Ken.begin() + j);
					break;
				}
			}
		}
	}
	return result;
}

int Dwar(vector<double> Naomi, vector<double> Ken, int N) {
	int result = 0;
	for (int i = 0; i < N; i++) {
		if (Naomi[i] > Ken[0]) {
			result++;
			Ken.erase(Ken.begin());
		} else {
			Ken.pop_back();
		}
	}
	return result;
}

void processCase(ifstream &infile, ofstream &outfile, int number) {
	int N;
	infile >> N;
	vector<double> Naomi(N, 0);
	vector<double> Ken(N, 0);
	for (int i = 0; i < N; i++) {
		infile >> Naomi[i];
	}
	for (int i = 0; i < N; i++) {
		infile >> Ken[i];
	}
	sort(Naomi.begin(), Naomi.end());
	sort(Ken.begin(), Ken.end());
	int war = War(Naomi, Ken, N);
	int dwar = Dwar(Naomi, Ken, N);
	outfile << "Case #" << number << ": " << dwar << ' ' << war << endl;
}