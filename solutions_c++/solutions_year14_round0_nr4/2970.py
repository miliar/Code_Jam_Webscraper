#include<cstring>
#include<cstdio>
#include<iostream>
#include<algorithm>

using namespace std;

const int mn = 1010;
const int mm = 1000000007;
const int MAX = 10000000;

int Test;
int n, m, t;
double a[mn], b[mn];
bool bo[mn];

int main()
{
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	cin >> Test;
	for ( int Testi = 0; Testi < Test; ++Testi )
	{
		cin >> n;
		for ( int i = 0; i < n; ++i ) cin >> a[i];
		for ( int i = 0; i < n; ++i ) cin >> b[i];
		sort( a, a + n );
		sort( b, b + n );
		int t = 0, w = n - 1;
		int ans = 0;
		for ( int i = 0; i < n; ++i )
		{
			if ( a[i] > b[t] )
				++t , ++ans;
			else
				--w;
		}
		cout << "Case #" << Testi+1 << ": " << ans;
		ans = 0;
		memset( bo, 0, sizeof bo );
		for ( int i = 0; i < n; ++i )
		{
			bool ok = false;
			for ( int j = 0; j < n; ++j ) if ( !bo[j] && b[j] > a[i] )
			{
				bo[j] = true;
				ok = true;
				break;
			}
			if ( !ok ) 
			{
				for ( int j = 0; j < n; ++j ) if ( !bo[j] )
				{
					bo[j] = true ;
					++ans;
					break;
				}
			}
		}
		cout << " " << ans << endl;
	}
}