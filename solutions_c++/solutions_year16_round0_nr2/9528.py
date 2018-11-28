#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main ()
{
	int tests;
	cin  >> tests;
	string S;
	for (int i = 0; i < tests; i++)
	{
		cin >> S;
		int flips = 0;
		for (int j = S.length()-1; j >= 0; j--)
		{
			if (((S[j] == '+') && (flips%2 == 0)) ||
			    ((S[j] == '-') && (flips%2 == 1)))
				continue;
			else
				flips ++;
		}
		cout << "Case #" << i + 1 << ": " << flips << "\n";
	}
}