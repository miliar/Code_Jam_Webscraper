#include <iostream>
#include <string>
using namespace std;

void run();

int main()
{
	long T;
	cin >> T;

	for (int c = 1; c <= T; ++c)
	{
		cout << "Case #" << c << ": ";
		run();
	}
}

void run()
{
	string S;
	cin >> S;

	string output = "";

	int len = S.length();
	for (int i = 0; i < len; ++i)
	{
		if (S[i] >= output[0])
			output = S[i] + output;
		else
			output += S[i];
	}

	cout << output << endl;
}