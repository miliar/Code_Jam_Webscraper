#include <stdio.h>
#include <iostream>
#include <cmath>
#include <sstream>
#include <string>

using namespace std;

bool esPalin(int j)
{
	string s;
	stringstream out;
	out << j;
	s = out.str();
	for (int i = 0; i < s.length() / 2; ++i)
		if (s[i] != s[s.length() - i - 1])
			return false;
	return true;
}

int main(int argc, char* argv)
{
	int T;
	cin >> T;
	for(int i = 1; i <= T; ++i)
	{
		int cantSF = 0;
		int A, B;
		cin >> A >> B;

		for(int j = A; j <= B; ++j)
		{
			cantSF += ((int)sqrt(j) * (int)sqrt(j) == j) && esPalin(j) && esPalin(sqrt(j));
		}

		cout << "Case #" << i << ": " << cantSF << endl;
	}
	return 0;
}