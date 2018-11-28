#include <bits/stdc++.h>
using namespace std;

const int TAM = 1010;

int n;
int bigger[TAM][TAM];
bool out[TAM];

int solve1 ( )
{
	int ans = 0;
	memset ( out, false, sizeof(bool)*TAM );
	for ( int i = n-1; i >= 0; --i ) {
		int minJ = -1;
		for ( int j = 0; j < n; ++j )
			if ( !out[j] ) {
				if ( !bigger[i][j] ) {
					out[j] = true;
					minJ = -1;
					break;
				}
				if ( minJ == -1 )
					minJ = j;
			}
		if ( minJ != -1 ) {
			out[minJ] = true;
			ans++;
		}
	}
	return ans;
}

int solve2 ( )
{
	int ans = 0;
	memset ( out, false, sizeof(bool)*TAM );
	for ( int i = 0; i < n; ++i )
	{
		int maxJ = -1;
		for ( int j = n-1; j >= 0; --j )
			if ( !out[j] ) {
				if ( bigger[i][j] ) {
					out[j] = true;
					maxJ = -1;
					ans++;
					break;
				}
				if ( maxJ == -1 )
					maxJ=j;
			}
		if ( maxJ != -1 ) {
			out[maxJ] = true;
		}
	}

	return ans;
}

int p10[6];
int readInt ( int& x ) {
	string s;
	cin >> s;
	x = 0;
	for ( int i = 2; i < s.size(); ++i )
		x += ((int)s[i]-'0')*p10[7-i];
}

int main ( )
{
	p10[0] = 1;
	for ( int i = 1; i < 6; ++i )
		p10[i] = p10[i-1]*10;

	int nTests;
	cin >> nTests;
	for ( int test = 1; test <= nTests; ++test )
	{
		cin >> n;
		vector<int> a(n), b(n);
		for ( int i = 0; i < n; ++i ) readInt(a[i]);
		for ( int i = 0; i < n; ++i ) readInt(b[i]);
		sort ( a.begin(), a.end() );
		sort ( b.begin(), b.end() );
		for ( int i = 0; i < n; ++i )
			for ( int j = 0; j < n; ++j )
				bigger[i][j] = ( a[i] > b[j] );

		cout << "Case #" << test << ": " << solve2() << " " << solve1() << endl;
	}
	return 0;
}
