#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <vector>
#include <chrono>

using namespace std;


using longlong = long long;


void addDigits(set<longlong> &theSet, longlong number)
{
	int digit;
	while (number != 0) {
		digit = number % 10L;

		if (theSet.find(digit) == theSet.end()) {
			theSet.insert(digit);
		}

		number /= 10L;
	}
}


longlong multiple(longlong n)
{
	if (n == 0) {
		return 0;
	}

	set<longlong> numberSet;
	int m = 1;
	addDigits(numberSet, n);

	for (m = 2; numberSet.size() < 10; ++m) {
		addDigits(numberSet, n * m);
	}

	return (m - 1) * n;
}

using namespace std::chrono;


int main(int argc, char *argv[])
{
	ifstream infile("A-large.in");
	ofstream outfile("output.txt");

	int caseCount;
	infile >> caseCount;

	longlong n;

	high_resolution_clock::time_point startTime = high_resolution_clock::now();

	for (int caseNum = 1; caseNum <= caseCount; ++caseNum) {
		infile >> n;
		longlong theMultiple = multiple(n);
		outfile << "Case #" << caseNum << ": ";

		if (theMultiple) {
			outfile << theMultiple << '\n';
		} else {
			outfile << "INSOMNIA\n";
		}
	}

	cout << "Time: " << duration_cast<nanoseconds>(high_resolution_clock::now() - startTime).count();
}
