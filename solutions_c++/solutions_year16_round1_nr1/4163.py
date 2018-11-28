#include <iostream>
#include <string>
#include <stdlib.h>

using namespace std;

int main ()
{
	int T;
	cin >> T;
	unsigned long long arr[11] = { 0 };

	for ( int k = 1; k <= T; k++ )
	{
		std::string S; 
		char O[1001];

		cin >> S;

		cout << "Case #" << k << ": ";
		int i = 0;
		for ( i = 0; i < S.length (); i++ )
		{
			if ( i == 0 )
				O[i] = S[i];
			else
			{
				if ( O[0] <= S[i] )
				{
					for ( int j = i; j > 0; j-- )
					{
						O[j] = O[j - 1];
					}
					O[0] = S[i];
				}
				else
					O[i] = S[i];
			}

		}
		O[i] = '\0';
		cout << O << endl;

	}
}