#include <bits/stdc++.h>
using namespace std;
 
typedef pair< int , int > pii;
typedef long long LL;
#define fr first
#define se second
#define EPS 1e-8
#define INF 10000*10000*10000LL
stringstream ss;
#define two(x) ( 1LL<<x )
LL mod = 1000000007LL;

/**************************Code****************************/


int main()
{
	int t, cc = 0;
	cin >> t;
	while( t -- )
	{
		int n;
		string s;
		cin >> n >> s;
		int tot = 0, add = 0;
		for( int i = 0 ; i <= n ; i ++ )
		{
			if( s[i] != '0' && tot + add < i )
				add += i - tot - add;
			tot += s[i]-'0';
		}
		cout << "Case #" << ++ cc << ": " << add << endl;
	}
	return 0;
}
