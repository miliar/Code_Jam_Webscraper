#include<bits/stdc++.h>
using namespace std;
int main()
{
	int tc;
	int ms;
	cin >> tc;
	for ( int i = 0 ; i < tc ; i ++ )
	{
		cin >> ms;
		string n ;
		cin >> n;
		int ans = 0 ;
		int cp = 0;
		bool flag = true;
		while ( true)
		{
			//cout << " here " << endl;
			
			for ( int j = 0 ; j < n.size() ; j ++ )
			{
				if ( n[j] == '0' )
					continue;
				if (cp >= j )
				{
					cp += n[j] - '0';
					n[j] = '0';
				}
				if ( n[j] != '0' ) 
				{
					flag = false;
				}
			}
			if ( flag )
				break;
			flag = true;
			ans ++ ;
			cp ++ ;
		}
		cout << "Case #"<<i+1<<": " << ans << endl;
	}
}
