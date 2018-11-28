#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <fstream>
#include <map>
#include <algorithm>

using namespace std;

void findMin(int A, list<int>& sizes, int& result) {
	if(sizes.size() == 0) {
		return;
	}
	int min = sizes.front();
	if(min < A) {
		sizes.pop_front();
		findMin(A + min, sizes, result);
	}
	else {
		/* 2 cases */
		if(A + A-1 > min) {
			//Add A-1, eat it, and start again 
			result += 1;
			A += (A-1);
			A += min;
			sizes.pop_front();
			findMin(A, sizes, result);
		}
		else if(A == 1) {
			result += sizes.size();
			return;
		}else {
			int result1 = result+1;
			int result2 = result+1;

			int A1 = A + A-1;;
			int A2 = A;
			list<int> sizes1 = sizes;
			list<int> sizes2 = sizes;
			sizes2.pop_front();
			findMin(A1, sizes1, result1);
			findMin(A2, sizes2, result2);
			result = std::min(result1, result2);
		}
	}
}

int main(int argc, char* argv[]) {
	string inTestName, outTestName;

	cout << "Enter the in test file name : " << endl;
	cin >> inTestName;
	cout << endl;

	size_t found = inTestName.find_last_of(".");
	outTestName = inTestName.substr(0, found) + ".out";

	/* Open file */
	ifstream inFile(inTestName.c_str());
	if(!inFile.is_open()) {
		cout << "Can't open input file" << endl;
		system("PAUSE");
		return 1;
	}

	ofstream outFile(outTestName.c_str());
	if(!outFile.is_open()) {
		cout << "Can't open output file" << endl;
		system("PAUSE");
		return 1;
	}

	int T; /*number of tests */
	inFile >> T;

	cout << "Start : "<< endl;
	for(int t = 0; t < T; t++) {
		cout << "\rProcess test " << t << " out of " << T;
		int A, N;
		inFile >> A >> N;
		list<int> sizes;
		for(int i = 0; i < N; i++) {
			int size;
			inFile >> size;
			sizes.push_back(size);
		}

		//sort
		sizes.sort();
		//std::sort(sizes.begin(), sizes.end());

		int result = 0;
		findMin(A, sizes, result);

		/* Check if X won */
		outFile << "Case #" << t + 1 << ": " << result << endl;
	}
	outFile.close();
	inFile.close();

	cout << endl << "Stop" << endl;

	system("PAUSE");
	return 0;
}
