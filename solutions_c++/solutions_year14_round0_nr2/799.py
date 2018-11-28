#include <bits/stdc++.h>
using namespace std;

int main ( )
{
	cin.tie(0);
	ios_base::sync_with_stdio(0);

	fixed(cout);
	cout.precision(7);

	double curTime, curRate, ans;
	double costFarm, farmRate, wanted;

	int nTests;
	cin >> nTests;
	for ( int test = 1; test <= nTests; ++test )
	{
		cin >> costFarm >> farmRate >> wanted;
		curTime=0; curRate=2; ans=1e100;

		while ( ans > curTime + wanted/curRate ) {
			ans = curTime + wanted/curRate;
			curTime += costFarm/curRate;
			curRate += farmRate;
		}

		cout << "Case #" << test << ": ";
		cout << ans;
		cout << '\n';
	}
	
	return 0;
}
