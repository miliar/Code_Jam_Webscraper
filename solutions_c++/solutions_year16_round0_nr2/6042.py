#include <iostream>
#include <string>
using namespace std;

int flips(string s)
{
	int moves = s[0] == '+' ? 0 : 1;

	for (int i=1; s[i]; ++i)
	{
		if (s[i] == '-' && s[i-1] == '+')
			moves += 2;
	}
	return moves;
}

int main()
{
	int t; cin >> t;
	string s;
	int i=1;

	while (t--)
	{
		cin >> s;
		cout << "Case #" << i++ << ": " << flips(s) << endl;
	}
	return 0;
}