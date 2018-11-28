#include <bits/stdc++.h>
using namespace std;

#define ff first
#define ss second
#define pb push_back

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> ii;

const int MAXN = 112;
const int INF = 0x3f3f3f;

int main()
{
	int T, N,tc = 1;
	cin >> T;
	while ( T-- ) {
		cin >> N;
		priority_queue< ii > pq;
		int x;
		for ( int i = 0; i < N; i++ ) {
			cin >> x;
			pq.push(ii(x,'A'+i));
		}
		cout << "Case #" << tc++ << ":";
		ii p1,p2;
		while ( !pq.empty() ) {
			p1 = pq.top(); pq.pop();
			p2 = pq.top(); pq.pop();
			if ( p2.first == 1 ) {
				pq.push(p1); pq.push(p2);
				break;
			}
			else {
				p1.first--;
				p2.first--;
				pq.push(p1); pq.push(p2);
				cout << " " <<  char(p1.second) << char(p2.second);
			}
		}
		while ( pq.top().first > 1 ) {
			p1 = pq.top(); pq.pop();
			p1.first--;
			pq.push(p1);
			cout << " " << char(p1.second);
		}
		if ( !(N%2) ) {
			for ( int i = 0; i+1 < N; i++ )
				cout << " " << char('A'+i) << char('A'+i+1);
		}
		else {
			for ( int i = 0; i < N-2; i++ )
				cout << " " << char('A'+i);
			cout << " " << char('A'+N-2) << char('A'+N-1);
		}
		cout << endl;
	}
	return 0;
}