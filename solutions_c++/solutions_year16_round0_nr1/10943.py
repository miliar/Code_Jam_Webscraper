#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

long long int lastNumberBeforeForSleep(long long int N);

int main()
{
	ifstream inf("A-large.in");
	ofstream outf("A-large.out");

	long long int N = 0;
	int count = 0;
	while (!inf.eof())
	{
		inf >> N >> ws;
		if (count == 0) {
			count++;
			continue;
		}

		long long int lastNumber = lastNumberBeforeForSleep(N);
		if (lastNumber == -1)
			outf << "Case #" << count << ": INSOMNIA" << endl;
		else
			outf << "Case #" << count << ": " << lastNumber << endl;

		count++;
	}
		

	return 0;
}

bool isDigitAllOk(bool* isDigitOccur, int n)
{
	for (int i = 0; i < n; i++) {
		if (isDigitOccur[i] == false)
			return false;
	}

	return true;
}

vector<int> getDigit(long long int number)
{
	int no = number;
	vector<int> digit;
	while (no >= 10) {
		int res = no % 10;
		digit.push_back(res);
		no = no / 10;
	}
	digit.push_back(no);

	return digit;
}

void checkDigit(vector<int> digit, bool* isDigitOccur)
{
	for (int i = 0; i < digit.size(); ++i) {
		isDigitOccur[digit[i]] = true;
	}
}

long long int lastNumberBeforeForSleep(long long int N)
{
	if (N == 0)
		return -1;

	bool isDigitOccur[10];
	for (int i = 0; i < 10; ++i)
		isDigitOccur[i] = false;

	int count = 1;
	while (isDigitAllOk(isDigitOccur, 10) == false)
	{
		vector<int> digit;
		digit = getDigit(N*count);

		checkDigit(digit, isDigitOccur);

		count++;
	}

	return N * (count - 1);
}



 