#include <bits/stdc++.h>
using namespace std;

#define fr first
#define se second

int main()
{
	int t, tc = 0;
	cin >> t;
	while( t -- )
	{
		int n, x, mn = 1000000, sum = 0;
		priority_queue < pair < int, int > > pq;
		cin >> n;
		for( int i = 0 ; i < n ; i ++ )
		{
			cin >> x, pq.push( make_pair( x, i ) );
			mn = min( mn, x );
			sum += x;
		}
		cout << "Case #" << ++ tc << ": ";
		while( pq.top().fr > mn )
		{
			int x = pq.top().fr, y = pq.top().se;
			pq.pop();
			if( x > 1 )
				pq.push( make_pair( x-1, y ) );
			cout << " " << char( 'A'+y );
			sum --;
		}
		if( sum % 2 )
		{
			int x = pq.top().fr, y = pq.top().se;
			pq.pop();
			if( x > 1 )
				pq.push( make_pair( x-1, y ) );
			cout << " " << char( 'A'+y );
			sum --;
		}
		while( !pq.empty() )
		{
			int x = pq.top().se, px = pq.top().fr;
			pq.pop();
			int y = pq.top().se, py = pq.top().fr;
			pq.pop();
			if( px > 1 )
				pq.push( make_pair( px-1, x ) );
			if( py > 1 )
				pq.push( make_pair( py-1, y ) );
			cout << " " << char('A'+x) << char('A'+y);
		}
		cout << endl;
	}
	return 0;
}