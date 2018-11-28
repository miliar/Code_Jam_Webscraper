#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

const int TAM = 8;
const int MOD = 1000000007;

int cost[1<<TAM];
pii dp[5][1<<TAM];
bool seen[5][1<<TAM];

int n;

pii go ( const int left, const int mask )
{
	pii& r = dp[left][mask];
	if ( seen[left][mask]++ ) return r;
	r = pii(-1,0);

	if ( left == 0 && mask+1 == (1<<n) ) return r = pii(0,1);
	if ( left == 0 ) return r;

	for ( int add = 0; add < (1<<n); ++add )
	{
		if ( mask&add ) continue;
		pii aux = go(left-1,mask|add);
		if ( aux.first < 0 ) continue;
		if ( aux.second == 0 ) continue;

		aux.first += cost[add];
		if ( aux.first == r.first ) r.second = (aux.second+r.second)%MOD;
		if ( aux.first > r.first ) r = aux;
	}

	return r;
}

int main ( )
{
//	cin.tie(0);
//	ios_base::sync_with_stdio(0);

	int nTests;
	cin >> nTests;

	for ( int curT = 1; curT <= nTests; ++curT )
	{
		int m;
		cin >> n >> m;
		vector<string> arr ( n );
		for ( int i = 0; i < n; ++i )
			cin >> arr[i];

		for ( int mask = 0; mask < (1<<n); ++mask ) {
			set<string> st;
			for ( int i = 0; i < n; ++i )
				if ( (mask>>i)&1 )
					for ( int j = 0; j <= int(arr[i].size()); ++j )
						st.insert ( arr[i].substr ( 0, j ) );
			cost[mask] = st.size();
		}

		memset ( seen, false, sizeof ( seen ) );
		cout << "Case #" << curT << ": " << go(m,0).first << ' ' << go(m,0).second << '\n';
	}

	return 0;
}
