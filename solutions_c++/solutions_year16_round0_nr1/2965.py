#include<iostream>
#include<vector>
#include<fstream>
using namespace std;
bool countSheep(int multiply, vector<int>&multiplier, int initNum,int& count) {
	long long res = (long long)initNum* (long long)multiply;
	if (res == 0)return false;
	while (res > 0) {
		int cur = res % 10;
		if (multiplier[cur] == 0) {
			count++;
			multiplier[cur] = multiply;
		}
		res /= 10;
	}
	return true;
}
int main() {
	ifstream infile("A-large.in");
	ofstream outfile("out.txt");
	int testCount = 0;
	infile >> testCount;
	for (int i = 0; i < testCount; i++) {
		int initNum = 0;
		infile >> initNum;
		bool isNeg = false;
		if (initNum < 0) {
			isNeg = true;
			initNum = -initNum;
		}
		int numCount = 0,multiply=1;
		vector<int>multiplier(10, 0);
		bool canSolve = true;
		while (numCount < 10) {
			if (!countSheep(multiply++, multiplier, initNum, numCount)) {
				canSolve = false;
				break;
			}
		}
		if (canSolve) {
			if (!isNeg)
				outfile << "Case #" << i+1 << ": " << ((long long)initNum*((long long)multiply - 1)) << endl;
			else
				outfile << "Case #" << i+1 << ": " << "-" << ((long long)initNum*((long long)multiply - 1)) << endl;
		}
		else
			outfile << "Case #" << i+1 << ": " << "INSOMNIA" << endl;
	}
	infile.close();
	outfile.close();
	return 0;
}