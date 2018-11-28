#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define all(x) x.begin(),x.end()
#define fastin std::ios::sync_with_stdio(false);cin.tie(nullptr)
#define cout_precision(x) cout<<std::fixed<<setprecision(x)
using namespace std;

int main()
{
	fastin;
	int t, sMax, testCase = 1;
	cin >> t;
	while ( t-- )
	{
		cin >> sMax;
		string sString;
		cin >> sString;
		vector<int> s( sMax + 1 );
		for ( int i = 0; i <= sMax; i++ )
		{
			s[i] = sString[i] - '0';
		}
		int peopleStanding = s[0];
		for ( int i = 1; i <= sMax; i++ )
		{
			if ( peopleStanding < i )
			{
				peopleStanding += i - peopleStanding;
			}
			peopleStanding += s[i];
		}
		cout << "Case #" << testCase++ << ": ";
		cout << peopleStanding - accumulate( all( s ), 0 ) << "\n";
	}
}
