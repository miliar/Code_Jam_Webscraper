#include <string>
#include <iostream>

using namespace std;


size_t calcNumMoves(string s)
{
	char prev;
	int i, end, changes;
	size_t len = s.length();
	const char *cs = s.c_str();
	
	for(end = len-1; end >= 0 && cs[end] == '+' ; end--);

	if(end < 0)
		return 0;

	for(i = 0, prev = cs[0], changes = 0; i <= end; i++)
	{
		if(prev != cs[i])
			changes++;

		prev = cs[i];
	}

	return changes+1;
}

void readFromStdin()
{
	int T;

	cin >> T;

	for(int t = 0; t < T; t++)
	{
		string s;

		cin >> s;

		cout << "Case #" << t+1 << ": " << calcNumMoves(s) << endl;
	}
}

int main()
{
	readFromStdin();
	return 0;
}
