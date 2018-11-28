#include <iostream>

using namespace std;

bool cnt[2501];

int main() 
{
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) 
	{
		int n;
		cin >> n;

		for( int j = 0; j < 2501; j++ )
			cnt[j] = false;
		
		for( int j = 0; j < ((2*n) - 1); j++ )
		{
			for( int k = 0; k < n; k++ )
			{
				int h = 0;
				cin >> h;

				cnt[h] = !cnt[h];
			}
		}

		cout << "Case #" << i+1 << ": ";
		for( int j = 0; j < 2501; j++ )
		{
			if( cnt[j] == true )
			{
				cout << j << " ";
			}
		}
		cout << endl;
	}

	return 0;
}