#include <iostream>
#include <string>
#include <fstream>

using namespace std;

ifstream fin( "C1.in" );
ofstream fout( "C1.out" );
#define cin fin
#define cout fout

int map[256];
string s, temp;
int M[4][4] = { {1, 2, 3, 4}, {2, -1, 4, -3}, {3, -4, -1, 2}, {4, 3, -2, -1}};

int mul( int c1, int c2 ){
	return M[c1 - 1][c2 - 1];
}

int arr[100000];
int l[1000000], r[1000000];

string f( int a ){
	string ret = "";
	if( a < 0 )
		ret += '-';
	a = abs( a );
	char aa[] = { '1', 'i', 'j', 'k' };
	return ret + aa[a - 1];
}

int main()
{
	int test;
	cin >> test;
	for( int T = 1; T <= test; T++ ){
		s = temp = "";
		int L, X;
		cin >> L >> X;
		for( int i = 0; i < L; i++ ){
			char c;
			cin >> c;
			s += c;
		}
		temp = s;
		for( int i = 0; i < X - 1; i++ )
			s += temp;
		for( int i = 0; i < s.length(); i++ ){
			char c = s[i];
			if( c == 'i' )
					arr[i] = 2;
			else if( c == 'j' )
					arr[i] = 3;
			else arr[i] = 4;
		}
		l[0] = arr[0];
		r[s.length() - 1] = arr[s.length() - 1];
		for( int i = 1; i < s.length(); i++ ){
			int sign = ( l[i - 1] < 0 ) ? -1 : 1;
			int ml = mul( abs( l[i - 1] ), arr[i] );
			l[i] = ml * sign;
		}
		for( int i = s.length() - 2; i >= 0; i-- ){
			int sign = ( r[i + 1] < 0 ) ? -1 : 1;
			int ml = mul( arr[i], abs( r[i + 1] ) );
			r[i] = ml * sign;
		}
		/*cout << s << endl;
		for( int i = 0; i < s.length(); i++ )
			cout << f( l[i] ) << ' ';
		cout << endl;
		for( int i = 0; i < s.length(); i++ )
			cout << f( r[i] ) << ' ';
		cout << endl;
		*/
		int res = 0;
		for( int left = 0; left < s.length(); left++ )
			for( int right = left + 2; right < s.length(); right++ )
				if( l[left] == 2 && r[right] == 4 && l[right - 1] == 4 ){
					res = 1;
					break;
				}
		cout << "Case #" << T << ": " << ( res ? "YES" : "NO" ) << endl;

	}
	return 0;
}