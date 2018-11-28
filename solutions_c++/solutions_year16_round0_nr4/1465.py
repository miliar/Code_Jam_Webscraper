#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t, cc = 0;
	cin >> t;
	while( t -- )
	{
		int K, C, S;
		cin >> K >> C >> S;
		cout << "Case #" << ++cc << ":";
		for( int i = 0 ; i < K ; i ++ )
			cout << " " << i+1;
		cout << endl;
	}
	return 0;
}
