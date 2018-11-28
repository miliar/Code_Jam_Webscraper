#include <iostream>
#include <string>

using namespace std;

void flip ( string& str, int end ) {
	for ( int i = 0; i <= end; i++ ) {
		if ( str[i] == '+' )
			str[i] = '-';
		else
			str[i] = '+';
	}
}

int main ()
{
	int T;
	cin >> T;

	for ( int i = 1; i <= T; i++ )
	{
		string str;
		cin >> str;

		int count = 0;

		for ( int j = str.length () - 1; j >= 0; j-- )
		{
			if ( str[j] == '-' )
			{
				flip ( str, j );
				count++;
			}
		}
		cout << "Case #" << i << ": " << count << endl;
	}
}