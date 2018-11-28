#include <iostream>
#include <sstream>
#include <cmath>
using namespace std;

bool isFair(unsigned long long number)
{
	bool val = true;

	stringstream stream;
	string s;
	stream << number;
	stream >> s;

	int i, len = s.length();
	for (i = 0; i < len / 2; ++i)
		if (s[i] != s[len - i - 1])
			val = false;

	return val;
}

void analyze(int id)
{
	unsigned long long A, B;
	cin >> A >> B;

	unsigned long long i;
	int count = 0;
	for (i = A; i <= B; ++i)
		if (isFair(i) && sqrt(i) == static_cast<unsigned long long>(sqrt(i)) && isFair(sqrt(i)))
			count++;

	cout << "Case #" << id << ": " << count << endl;
}

int main(int argc, char* argv[])
{
	int i, test = 0;
	cin >> test;
	for (i = 0; i < test; ++i)
		analyze(i + 1);
	return 0;
}