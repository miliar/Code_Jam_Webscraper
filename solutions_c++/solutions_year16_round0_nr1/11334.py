#include <iostream>
#include <fstream>
#include <cstring>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <iterator>
#include <algorithm>
#include <ctime>

using namespace std;

const char *fninp = "A-small-attempt3.in";
const char *fnout = "A-small-attempt3.out";
// const char *fninp = "A.inp";
// const char *fnout = "A.out";
const string NO_SOLUTION = "INSOMNIA";
const int LIMIT = 1e6;

ifstream finp;
ofstream fout;

int nTests;

long long search(int N) {
	bool *marked = new bool [10];
	memset(marked, false, sizeof(marked));
	for (int j = 0; j < 10; ++j) {
		marked[j] = false;
	}
	
	for (int i = 1; i <= LIMIT; ++i) {
		long long number = (long long)(N) * (long long)(i);
		while (number > 0) {
			int digit = number % 10;
			number /= 10;
			marked[digit] = true;
		}
		
		bool stop = true;
		for (int j = 0; j < 10; ++j) {
			if (marked[j] == false) {
				stop = false;
				break;		
			}
		}
		if (stop) {
			return (long long)(N) * (long long)(i);
		}
	}
	
	return -1;
}

void process() {
	finp >> nTests;
	int N;
	for (int test = 1; test <= nTests; ++test) {
		finp >> N;
		
		if (N == 0) {
			fout << "Case #" << test << ": " << NO_SOLUTION << endl;
			continue;
		}
		
		long long result = search(N);
		
		if (result == -1) {
			fout << "Case #" << test << ": " << NO_SOLUTION << endl;
		} else {
			fout << "Case #" << test << ": " << result << endl;
		}
	}
}

int main(int argc, char *argv[]) {
	finp.open(fninp, ios::in);
	fout.open(fnout, ios::out);
	
	process();
	
	finp.close();
	fout.close();
	
	return 0;
}
