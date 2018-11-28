#include <iostream>
#include <istream>
#include <fstream>

using namespace std;

bool TrackDigits(int & nDigitsAppear, bool appear[10], long long multipleN)
{
	while (multipleN) {
		int digit = multipleN % 10;
		if (!appear[digit]) {
			appear[digit] = true;
			nDigitsAppear++;
			if (nDigitsAppear == 10)
				return true;
		}
		multipleN /= 10;
	}
	return false;
}

int main()
{
	int T; int N;

	ifstream file("input.txt");
	ofstream output("output.txt");
	file >> T;
	int nT = 1;
	while (T--) {
		file >> N;

		bool appear[10] = { false };
		int nDigitsAppear = 0;
		long long nFound = -1;

		for (int i = 1; i < 1000000; i++) {
			long long multipleN = long long(N) * i;

			if (TrackDigits(nDigitsAppear, appear, multipleN)) {
				// end.
				nFound = multipleN;
			}
		}
		if (nFound < 0) {
			output << "Case #" << nT << ": " << "INSOMNIA" << endl;
		}
		else
			output << "Case #" << nT << ": " << nFound << endl;
		nT++;
	}

	return 0;
}