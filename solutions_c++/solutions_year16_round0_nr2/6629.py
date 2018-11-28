#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
	int testCases;
	long long int N, K; //Starting variables
	string S, b; //Starting variables
	cin >> testCases;

	int t = 1;
	while (testCases--)
	{
		cin >> S;
		//Either make all characters positive or negative
		bool previousPositive = true;
		long long int count = 0;
		for (int i = 0; i < S.length(); i++)
		{
			if (i == 0)
			{
				if (S[i] == '-')
					previousPositive = false;
			}
			else
			{
				if ((previousPositive && S[i] == '+') ||
					(!previousPositive && S[i] == '-'))
				{
					//Do nothing
				}
				else
				{
					//Toggle all pan cakes before
					count++;
					previousPositive = !previousPositive;
				}
			}
		}

		if (!previousPositive)
			count++;
		cout << "Case #" << t << ": " << count << endl;
		t++;
	}

	return 0;
}