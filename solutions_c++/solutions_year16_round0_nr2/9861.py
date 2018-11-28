#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair< string, ll > psl;

int T, nCase, sz;
string S, curS, newS, revS;

bool check( string &s ){
	for( int i = 0; i < sz; i++ )
		if( s[i] == '-' ) return false;
	return true;
}

void flip( string &s ){
	for( int i = 0; i < sz; i++ )
		s[i] = (s[i] == '+') ? '-' : '+';
}

ll solve(){

	if( check(S) ) return 0LL;

	queue< psl > q;
	set< string > visited;
	q.push( make_pair(S, 0LL) );
	visited.insert(S);
	ll depth;

	while( !q.empty() ){
		curS = q.front().first;
		depth = q.front().second;
		q.pop();

		revS = curS;
		reverse( revS.begin(), revS.end() );
		flip( revS );
		for( int i = 0; i < sz; ++i ){
			//cout << "ini" << endl;
			//cout << "len: " << curS.length() << ", pos: " << (sz-i) << ", i: " << i << endl;
			newS = revS + curS.substr( sz-i, i );
			//cout << "sal" << endl;
			revS = revS.substr( 1, sz-i-1 );
			if( visited.count( newS ) ) continue;
			if( check( newS ) ) return depth + 1LL;
			visited.insert( newS );
			q.push( make_pair( newS, depth+1LL ) );
		}
	}

	return depth;

}

int main(){

	cin >> T;

	while( T-- ){
		cin >> S;
		sz = S.length();
		cout << "Case #" << ++nCase << ": " << solve() << endl;
	}

	return 0;
}