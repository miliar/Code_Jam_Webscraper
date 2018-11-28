#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

bool FlipOnce( string& s, int k ) // Return true if we should keep going
{
	int i = 0;
	while ( i < s.size() && s[i] == '+' )
		++i;
	if ( i == s.size() )
		return false;
	if ( i > s.size() - k )
		return false;
	for ( int ii = i; ii < i + k; ++ii )
	{
		if ( s[ii] == '+' )
			s[ii] = '-';
		else
			s[ii] = '+';
	}
	return true;
}

int main()
{
	ifstream input("input.txt");
	ofstream output("output.txt");
	int T; input >> T;
	for ( int c = 1; c <= T; ++c )
	{
		string s; input >> s;
		int k; input >> k;

		int answer = 0;
		while ( FlipOnce( s, k ) )
		{
			++answer;
		}
		output << "Case #" << c << ": ";
		bool success = true;
		for ( char ch : s )
		{
			if ( ch != '+' )
			{
				success = false;
				break;
			}
		}
		if ( success )
			output << answer << endl;
		else
			output << "IMPOSSIBLE" << endl;
	}
	input.close();
	output.close();
	cout << "\ndone";
	cin >> T;
}