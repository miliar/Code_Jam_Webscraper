#include <bits/stdc++.h>

using namespace std;

#define REP(i , a) for (int i = 0 ; i < (a) ; i++ )

int solve ()
{
	int s , alreadyStanding = 0, needMore = 0 , totalNeedMore = 0;
	char str[1003];
	cin >> s >> str;
	alreadyStanding = str[0] - '0';
	for ( int i = 1 ; i <= s ; i++ )
	{
		if ( str[i] != '0' && alreadyStanding < i )
		{
			needMore = i - alreadyStanding;
			totalNeedMore += needMore;
			alreadyStanding += needMore;
		}
		alreadyStanding += str[i] - '0';
	}
	return totalNeedMore;
}

int main ()
{
	int t , ans;
	cin >> t;
	for ( int z = 1 ; z <= t ; z++ )
	{
		ans = solve ();
		cout << "Case #" << z << ": " << ans << endl;
	}
	return 0;
}
