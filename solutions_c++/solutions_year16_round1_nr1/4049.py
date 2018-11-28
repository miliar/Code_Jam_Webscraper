#include <iostream>
#include <string>
using namespace std;

string solve(const string& seq)
{
	string sol;
	char maximum = 'A';
	for (int k = 0; k < seq.size(); k++)
	{
		if (seq[k] < maximum)
		{
			sol.insert(sol.end(), seq[k]);
		}
		else
		{
			sol.insert(sol.begin(), seq[k]);
			maximum = seq[k];
		}
	}
	return sol;
}

int main()
{
	int cases;
	string word;
	cin >> cases;
	for (int t = 1; t <= cases; t++)
	{
		cin >> word;
		cout << "Case #" << t << ": " << solve(word) << endl;
	}
	return 0;
}