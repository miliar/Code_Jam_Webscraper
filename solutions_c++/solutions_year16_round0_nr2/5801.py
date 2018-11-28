#include <iostream>
#include <string.h>

using namespace std;


int main(void)
{
	char S[200];
	int T;
	int t;
	char c;
	char lastc;
	int moves;
	
	
	cin >> T;
	cin.ignore(1);
	t = 1;
	while (t <=T)
	{
		cin.getline (S,150);
		moves = 0;
		lastc = '+';
		for (int i=strlen(S)-1;i>=0;i--)
		{
			c = S[i];
			if ( c != lastc )
			{
				moves++;
			}
			lastc = c;
		}
		cout << "Case #" << t << ": " << moves << endl;
		t++;
	}
	return 0;
}