#include <iostream>
#include <string>
#include <fstream>
using namespace std;

bool isDirectionAligned(char state, bool direction) {
	if ((state == '-') && (direction == false)) {
		return true;
	}
	else if ((state == '+') && (direction == true)) {
		return true;
	} 
	else {
		return false;
	}
}

int countNoOfFlips(const std::string & sequence) {
	bool direction = true;
	int flipCount = 0;
	int seqLen = static_cast<int>(sequence.length());
	for (int i = seqLen - 1; i >= 0; i--) {
		if (!isDirectionAligned(sequence[i], direction)) {
			flipCount++;
			direction = (!direction);
		}
	}
	return flipCount;
}
int main()
{
	std::ifstream infile("C:\\Users\\Reyansh\\Downloads\\A-small-attempt0.in");
	std::ofstream outfile("C:\\Users\\Reyansh\\Downloads\\B-Small.out");
	int nInputs;
	infile >> nInputs;
	std::string sequence;
	for (int i = 0; i < nInputs; i++) {
		infile >> sequence;
		//cout << sequence << endl;
		outfile << "Case #" << i + 1 << ": " << countNoOfFlips(sequence) << endl;
	}
	outfile.flush();
	infile.close();
	outfile.close();
    return 0;
}
