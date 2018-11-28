#include <iostream>
#include <ios>
#include <fstream>
#include <string>
#include <sstream>
#include <cstring>
#include <cstdlib>
#include <set>
#include <bitset>

using namespace std;

void getDigits(int n, set<int> &digits)
{
	while (n > 9) {
		int remainder = n % 10;
		digits.insert(remainder);
		n /= 10;
	}
	digits.insert(n);
}

int countNumber(int n)
{
	bitset<10> bs(0xffff);
	int count = 1;
	int lastNumber = n;
	while (bs.any()) {
		lastNumber = count * n;
		set<int> digits;
		getDigits(lastNumber, digits);
		for (set<int>::iterator iter = digits.begin(); iter != digits.end(); ++iter) {
			bs.reset(*iter);
		}
		++count;
	}
	return lastNumber;
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
		getline(inputFile, line);
		int n = atoi(line.c_str());

		if (n == 0) {
			outputFile << "Case #" << ++i << ": " << "INSOMNIA" << endl;
		}
		else {
			int count = countNumber(n);
			outputFile << "Case #" << ++i << ": " << count << endl;
		}
	}
	outputFile.flush();
	inputFile.close();
	outputFile.close();
	return 0;
}
