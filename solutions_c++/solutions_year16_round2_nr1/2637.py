#include <bits/stdc++.h>

using namespace std;

int T, nCase, len, curCnt;
string S;
int cnt[10];

void solve(){
	map<char, int> m;
	memset( cnt, 0, sizeof(cnt) );
	for( int i = 0; i < len; i++ )
		m[ S[i] ]++;

	if( m.count('Z') ){
		curCnt = m['Z'];
		//cout << "Z->" << curCnt;
		cnt[0] += curCnt;
		m[ 'Z' ] -= curCnt;
		m[ 'E' ] -= curCnt;
		m[ 'R' ] -= curCnt;
		m[ 'O' ] -= curCnt;
	}

	if( m.count('W') ){
		curCnt = m['W'];
		//cout << "W->" << curCnt;
		cnt[2] += curCnt;
		m[ 'T' ] -= curCnt;
		m[ 'W' ] -= curCnt;
		m[ 'O' ] -= curCnt;
	}

	if( m.count('U') ){
		curCnt = m['U'];
		//cout << "U->" << curCnt;
		cnt[4] += curCnt;
		m[ 'F' ] -= curCnt;
		m[ 'O' ] -= curCnt;
		m[ 'U' ] -= curCnt;
		m[ 'R' ] -= curCnt;
	}

	if( m.count('X') ){
		curCnt = m['X'];
		//cout << "X->" << curCnt;
		cnt[6] += curCnt;
		m[ 'S' ] -= curCnt;
		m[ 'I' ] -= curCnt;
		m[ 'X' ] -= curCnt;
	}

	if( m.count('G') ){
		curCnt = m['G'];
		//cout << "G->" << curCnt;
		cnt[8] += curCnt;
		m[ 'E' ] -= curCnt;
		m[ 'I' ] -= curCnt;
		m[ 'G' ] -= curCnt;
		m[ 'H' ] -= curCnt;
		m[ 'T' ] -= curCnt;
	}

	if( m.count('H') && m['H'] ){
		curCnt = m['H'];
		//cout << "H->" << curCnt;
		cnt[3] += curCnt;
		m[ 'T' ] -= curCnt;
		m[ 'H' ] -= curCnt;
		m[ 'R' ] -= curCnt;
		m[ 'E' ] -= curCnt;
		m[ 'E' ] -= curCnt;
	}

	if( m.count('F') && m['F'] ){
		curCnt = m['F'];
		//cout << "F->" << curCnt;
		cnt[5] += curCnt;
		m[ 'F' ] -= curCnt;
		m[ 'I' ] -= curCnt;
		m[ 'V' ] -= curCnt;
		m[ 'E' ] -= curCnt;
	}

	if( m.count('S') && m['S'] ){
		curCnt = m['S'];
		//cout << "S->" << curCnt;
		cnt[7] += curCnt;
		m[ 'S' ] -= curCnt;
		m[ 'E' ] -= curCnt;
		m[ 'V' ] -= curCnt;
		m[ 'E' ] -= curCnt;
		m[ 'N' ] -= curCnt;
	}

	if( m.count('I') && m['I'] ){
		curCnt = m['I'];
		//cout << "I->" << curCnt;
		cnt[9] += curCnt;
		m[ 'N' ] -= curCnt;
		m[ 'I' ] -= curCnt;
		m[ 'N' ] -= curCnt;
		m[ 'E' ] -= curCnt;
	}

	if( m.count('O') && m['O'] ){
		//cout << "W->" << curCnt;
		cnt[1] += m['O'];
	}

	for( int i = 0; i < 10; i++ )
		for( int j = 0; j < cnt[i]; j++ )
			cout << i;

}

int main(){

	ios_base::sync_with_stdio( 0 );
	cin.tie( 0 );

	freopen( "input", "r", stdin );
	freopen( "output", "w", stdout );

	cin >> T;

	while( T-- ){
		cin >> S;
		len = S.length();
		cout << "Case #" << ++nCase << ": ";
		solve();
		cout << endl;
	}


	return 0;
}