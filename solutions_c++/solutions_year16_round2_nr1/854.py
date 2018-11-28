#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t, tc = 0;
	cin >> t;
	while( t -- )
	{
		int ans[10] = {0};
		map < char, int > cnt;
		string s;
		cin >> s;
		for( int i = 0 ; i < s.size() ; i ++ )
			cnt[ s[i] ] ++;
		while( cnt[ 'Z' ] )
		{
			cnt[ 'Z' ] --;
			cnt[ 'E' ] --;
			cnt[ 'R' ] --;
			cnt[ 'O' ] --;
			ans[0] ++;
		}
		while( cnt[ 'W' ] )
		{
			cnt[ 'T' ] --;
			cnt[ 'W' ] --;
			cnt[ 'O' ] --;
			ans[2] ++;
		}
		while( cnt[ 'U' ] )
		{
			cnt[ 'F' ] --;
			cnt[ 'O' ] --;
			cnt[ 'U' ] --;
			cnt[ 'R' ] --;
			ans[4] ++;
		}
		while( cnt[ 'X' ] )
		{
			cnt[ 'S' ] --;
			cnt[ 'I' ] --;
			cnt[ 'X' ] --;
			ans[6] ++;
		}
		while( cnt[ 'G' ] )
		{
			cnt[ 'E' ] --;
			cnt[ 'I' ] --;
			cnt[ 'G' ] --;
			cnt[ 'H' ] --;
			cnt[ 'T' ] --;
			ans[8] ++;
		}
		while( cnt[ 'O' ] )
		{
			cnt[ 'O' ] --;
			cnt[ 'N' ] --;
			cnt[ 'E' ] --;
			ans[1] ++;
		}
		while( cnt[ 'T' ] )
		{
			cnt[ 'T' ] --;
			cnt[ 'H' ] --;
			cnt[ 'R' ] --;
			cnt[ 'E' ] --;
			cnt[ 'E' ] --;
			ans[3] ++;
		}
		while( cnt[ 'F' ] )
		{
			cnt[ 'F' ] --;
			cnt[ 'I' ] --;
			cnt[ 'V' ] --;
			cnt[ 'E' ] --;
			ans[5] ++;
		}
		while( cnt[ 'V' ] )
		{
			cnt[ 'S' ] --;
			cnt[ 'E' ] --;
			cnt[ 'V' ] --;
			cnt[ 'E' ] --;
			cnt[ 'N' ] --;
			ans[7] ++;
		}
		while( cnt[ 'N' ] )
		{
			cnt[ 'N' ] --;
			cnt[ 'I' ] --;
			cnt[ 'N' ] --;
			cnt[ 'E' ] --;
			ans[9] ++;
		}
		cout << "Case #" << ++tc << ": ";
		for( int i = 0 ; i < 10 ; i ++ )
			while( ans[i] -- )
				cout << i;
		cout << endl;
	}
	return 0;
}
