#include<iostream>
#include<string>
#include<algorithm>
#include<cstring>
#include<vector>
using namespace std;
int a[1000004];
long long dp[1000005];
bool ch ( char x)
{
	return ( x!='a' && x != 'e' && x != 'i' && x != 'o' && x != 'u' );
}
int main()
{
	int t,o=0;
	cin >>t;
	while ( t-- )
	{
		o++;
		string s;
		long long ans = 0,h=0;
		int n;
		cin >> s >> n;
		int l = s.size(), i, j;
		//int h;
		for ( i = 0; i < l; i++ )
		{
			h = 0;
			for ( j = i; j < l; j++ )
			{
				if ( ch(s[j]) )
				h++;
				else
				h=0;
				if ( h >= n )
				{
				ans+=(l-j);
				break;
				}
			}
		}
		cout << "Case #"<<o<<": "<<ans << endl;
	}
}
