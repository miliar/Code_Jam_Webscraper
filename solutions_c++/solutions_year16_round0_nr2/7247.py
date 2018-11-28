#include <iostream>
#include <string>

using namespace std;

int main(int argc, char const *argv[])
{
	int T(0);

	cin >> T;

	for (int i = 1; i <= T; ++i)
	{
		string S;
		cin >> S;

		char expectation('+');
		int flip_count(0);
		for (string::reverse_iterator j = S.rbegin(); j != S.rend(); ++j)
		{
			if (*j != expectation)
			{
				++flip_count;
				expectation = expectation == '+'?'-':'+';
			}
		}

		cout << "Case #" << i << ": " << flip_count << '\n';
	}

	return 0;
}