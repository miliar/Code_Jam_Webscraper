#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int t;
	cin >> t;
	for ( int tc = 1 ; tc <= t ; ++tc )
	{
		string s;
		cin >> s;
		int ans = 0;
		while (true )
		{
		//	cout << s << endl;
			bool flag = false;
			for ( int i = 0 ; i < s.size() ; i ++ )
			{
				if (s[i] == '-' )
					break;
				if ( i == s.size() - 1 )
					flag = true;
			}		
			if ( flag )
				break;
			string sc = s;
		
			bool flags = false;
			for ( int i = 0 ; i < s.size() ; i ++ )
			{
				if (s[i] == '+')
				{
					if (!flags)
						ans++,flags=true;
					s[i] = '-';
					continue;
				}
				break;

			}
			int ind = -1;
			for ( int i = s.size() -1 ; i >= 0 ; --i )
			{
				if ( s[i] == '-')
				{
				//	cout << "hereee " << i << endl;
					ind = i;
					break;
				}
			}
			sc = s;
			for ( int i = ind , j =0 ; i >= 0 ; --i , ++j)
			{
				char tmp;
				if (sc[i] == '-')
					tmp = '+';
				else 
					tmp = '-';
				s[j] = tmp;
			}	
			if (ind != -1 )
				ans ++;
		}
		cout << "Case #" <<tc << ": " << ans << endl;  
	}
	return 0;
}
