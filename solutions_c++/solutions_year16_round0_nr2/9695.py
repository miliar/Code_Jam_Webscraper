#include <iostream>
#include <string>

using namespace std;

const int YET = -1;
const int MINUS = 0, PLUS = 1;
const int SZ_LEN = 100 + 1, SZ_T_SIGN = 2, SZ_B_SIGN = 2;

int memo[SZ_LEN][SZ_T_SIGN][SZ_B_SIGN] = { 0 };

int rec ( int len, int t_sign, int b_sign )
{
	if ( memo[len][t_sign][b_sign] != YET ) {
		return memo[len][t_sign][b_sign];
	}
	if ( ( t_sign == PLUS ) && ( b_sign == PLUS ) ) {
		return memo[len][t_sign][b_sign] = rec( len - 1, PLUS, MINUS );
	}
	if ( ( t_sign == PLUS ) && ( b_sign == MINUS )) {
		return memo[len][t_sign][b_sign] = 1 + rec( len - 1, MINUS, MINUS );
	}
	if ( ( t_sign == MINUS ) && ( b_sign == PLUS )) {
		return memo[len][t_sign][b_sign] = rec( len - 1, MINUS, MINUS );
	}
	if ( ( t_sign == MINUS ) && ( b_sign == MINUS )) {
		return memo[len][t_sign][b_sign] = 1 + rec( len, PLUS, PLUS );
	}
}

void init ( void )
{
	for ( int i = 0; i < SZ_LEN; ++i ) {
		for ( int j = 0; j < SZ_T_SIGN; ++j ) {
			for ( int k = 0; k < SZ_B_SIGN; ++k ) {
				memo[i][j][k] = YET;
			}
		}
	}
	memo[1][PLUS][PLUS] = 0;
	memo[1][MINUS][MINUS] = 1;
}

void solve ( void )
{
	string s;
	int len, t_sign, b_sign;

	cin >> s;

	len = 1;
	for ( int i = 1; i < s.size(); ++i ) {
		if ( s[i] != s[i - 1] ) {
			++len;
		}
	}

	t_sign = ( s[0] == '+' ? PLUS : MINUS );
	b_sign = ( s[s.size() - 1] == '+' ? PLUS : MINUS );

	cout << rec( len, t_sign, b_sign );
}

int main ( void )
{
	// cin.tie( 0 );
	// ios::sync_with_stdio( false );
	int T;

	cin >> T;

	init();

	for ( int t = 1; t <= T; ++t ) {
		cout << "Case #" << t << ": ";
		solve();
		cout << endl;
	}
	return 0;
}
