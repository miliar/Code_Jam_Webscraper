#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main ( )
{
	cin.tie(0);
	ios_base::sync_with_stdio(0);

	int nTests;
	cin >> nTests;

	for ( int curT = 1; curT <= nTests; ++curT )
	{
		int ans = 0;

		int n, cap;
		cin >> n >> cap;

		vector<int> a(n);
		for ( int i = 0; i < n; ++i )
			cin >> a[i];
		sort ( a.begin(), a.end() );

		vector<bool> used(n,false);

		for ( int i = n-1, j=0; i >= 0; --i ) {
			if ( used[i] ) continue;
			used[i] = true;
			if ( a[i]+a[j] <= cap ) used[j++] = true;
			ans++;
		}

		cout << "Case #" << curT << ": " << ans << '\n';
	}

	return 0;
}
