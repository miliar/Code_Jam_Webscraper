#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

bool trueArray(bool array[]) {
	for (int i = 0; i < 10; i++)
	{
		if (array[i] == false) return false;
	}
	return true;
}

void checkDigits(bool array[], unsigned long n) {
	do
	{
		array[n % 10] = true;
		n /= 10;
	} while (n != 0);
}

unsigned long goSleep(unsigned long n) {
	if (n == 0) return 0;
	else
	{
		bool digits[10] = { false, false, false, false, false, false, false, false, false, false };
		unsigned long answer = 0;
		do
		{
			answer += n;
			checkDigits(digits, answer);
		} while (!trueArray(digits));
		return answer;
	}
}

int main() {
	ifstream inputFile;
	inputFile.open("input.txt");
	ofstream outputFile;
	outputFile.open("output.txt");
	int T;
	unsigned long N, answer;
	inputFile >> T;
	for (int i = 1; i <= T; i++)
	{
		cout << i << endl;
		inputFile >> N;
		answer = goSleep(N);
		if (answer == 0) outputFile << "Case #" << i << ": INSOMNIA\n";
		else outputFile << "Case #" << i << ": " << answer << "\n";
	}
}