#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;

int i, j, k, m, n, l, out;

string alphabet[26] = { "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z" };

int division[50];

int maxP(int numParties) {
	int max = 0;
	size_t maxIdx;
	for(size_t i = 0; i != numParties; i++) {
		if (division[i] > max) {
			max = division[i];
			maxIdx = i;
		}
	}
	return maxIdx;
}

int sumP(int numParties) {
	int sum = 0;
	for(size_t i = 0; i != numParties; i++) {
		sum += division[i];
	}
	return sum;
}

void doSomething(int numParties, string inp) {
	size_t bla = 0;

	for(char& c : inp) {
		if (c != ' ')
			division[bla++] = c - '0';
	}
	
	size_t idx = 0;
	while (sumP(numParties) > 0) {
		if (sumP(numParties) == 1 && idx == 0) {
			cout << alphabet[maxP(numParties)];
		}

		if (sumP(numParties) == 3 && idx == 0) {
			int max = maxP(numParties);
			division[max] = division[max] - 1;
			cout << alphabet[max];
			cout << " ";
			idx = 0;
		}
		else {
			int max = maxP(numParties);
			division[max] = division[max] - 1;
			cout << alphabet[max];
			if(++idx == 2) {
				idx = 0;
				cout << " ";
			}
		}
	}
	
	cout << '\n';
}

int main(int argc, char *argv[])
{
	string line = "";
	int caseNum = 1;
	getline(cin,line);
	int numItems = stoi(line);
	while (caseNum <= numItems) {
		cout << "Case #" + to_string(caseNum) + ": ";

		getline(cin, line);
		int numParties = stoi(line);

		getline(cin, line);

		doSomething(numParties, line);
		caseNum++;
	}
}