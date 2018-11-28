#include <iostream>
#include <string>

using namespace std;

int main()
{
	int N;
	cin >> N;

	for (int nTestCase = 1; nTestCase <= N; nTestCase++)
	{
		string S;
		do
			getline(cin, S);
		while (S.empty());

		char last = '+';
		int flips = 0;
		for (int i = S.length() - 1; i >= 0; i--)
			if (S[i] != last)
			{
				flips++;
				last = S[i];
			}

		cout << "Case #" << nTestCase << ": " << flips << endl;
	}

	return 0;
}
