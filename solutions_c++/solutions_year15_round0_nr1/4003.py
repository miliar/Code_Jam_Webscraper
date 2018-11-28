#include <bits/stdc++.h>
using namespace std;

#define maxsiz 1000000
#define mod 1000000007
#define F first
#define S second
#define si(a) scanf("%d",&a)
#define sl(a) scanf("%llu",&a)
#define pi(a) printf("%d",a)
#define pl(a) printf("%llu",a)
#define fr(i,k,n) for(int i = k ; i < n ; i++ )
#define mp(a,b) make_pair(a,b)
#define pb(a) push_back(a)
#define printvect(a,n) fr(i,0,n) cout << a[i] << " " ;
typedef unsigned long long int ull;

int main()
{
	int test,sm;
	cin >> test ;
	fr(t,0,test)
	{
		cin >> sm ;
		vector<char> s(sm+1) ;
		fr(i,0,sm+1)
			cin >> s[i];
		int ans = 0 ;
		int cumu = 0 ;
		fr(i,0,sm+1)
		{
			if( s[i] != '0')
			{
				if( cumu < i )
				{
					ans += i - cumu ;
					cumu += ( i-cumu );
				}
				cumu += (int)(s[i]-'0');
			}
		}
		cout << "Case #" << t+1 << ": " << ans << endl;
	}
	return 0 ;
}