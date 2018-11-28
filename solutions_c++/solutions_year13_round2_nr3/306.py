#include <fstream>
#include <iostream>
#include <string>
#include <fstream>
#include <set>
#define INF 1000000
using namespace std;

ifstream fin( "C-small-attempt1.in" );
ofstream fout( "C1.out" );

#define cin fin
#define cout fout


set< string > st;
ifstream ffin( "garbled_email_dictionary.txt" );
int T = 1, test, n;
string p;
int dp[5000][20];
#define P pair< int, int >
int zero[5000][11];
int one[5000][11][11];
int two[5000][11][11][11];

// idx, ta koja, aghab, akhar
P nx[5000][20];


int solve( int idx, int last ){
	if( idx == n )
		return 0;
	int& ref = dp[idx][last];
	if( ref != -1 )
		return ref;
	ref = INF;
	for( int j = 0; j <= 10; j++ ){
		if( idx + j >= n )
			break;
		if( zero[idx][j] ){
			//cout << idx << ' ' << idx + j + 1 << ' ' << endl;
			if( ref > solve( idx + j + 1, min( last + j + 1, 5 ) ) ){
				nx[idx][j] = P( idx + j + 1, min( last + j + 1, 5 ) );
			}
			ref = min( ref, solve( idx + j + 1, min( last + j + 1, 5 ) ) );
		}
		int st = 5 - last;
		for( int k = st; k <= j; k++ ){
			if( one[idx][j][k] ){
				ref = min( ref, 1 + solve( idx + j + 1, min( 5, j + 1 - k ) ) );
				break;
			}
			for( int z = k + 5; z <= j; z++ )
				if( two[idx][j][k][z] ){
					ref = min( ref, 2 + solve( idx + j + 1, min( 5, j + 1 - z ) ) );
					break;
				}
		}
	}
	return ref;
}



int main()
{
	int mx = 0;
	string s;
	while( ffin >> s ){
		mx = max( mx, (int)s.length() );
		st.insert( s );
	}
	for( cin >> test; test--; ){
		cerr << test << endl;
		memset( dp, -1, sizeof dp );
		memset( zero, 0, sizeof zero );
		memset( one, 0, sizeof one );
		memset( two, 0, sizeof two );
		cin >> p;
		n = p.size();
		for( int i = 0; i < n; i++ ){
			string now;
			for( int j = 0; i + j < n && j <= 10; j++ ){
				now += p[i + j];
				string temp = now;
				if( st.count( now ) ){
					zero[i][j] = 1;
					continue;
				}
				for( int k = 0; k < now.length(); k++ ){
					char ch = now[k];
					for( char z = 'a'; z <= 'z' ; z++ ){
						now[k] = z;
						if( st.count( now ) ){
							one[i][j][k] = 1;
							break;
						}
						for( int k2 = k + 5; k2 < now.length(); k2++ ){
							char ch2 = now[k2];
							for( char z2 = 'a'; z2 <= 'z'; z2++ ){
								now[k2] = z2;
								if( st.count( now ) ){
									two[i][j][k][k2] = 1;
									break;
								}
							}
							now[k2] = ch2;
							if( two[i][j][k][k2] )
								break;			
						}
					}
					now[k] = ch;
					//if( one[i][j][k] )
					//	break;
					
				}
			}
		}
		cout << "Case #" << T++ << ": " << solve( 0, 5 ) << endl;
		/*int a = 0, b = 5;
		while( a != n ){
			break;
			cout << "FGFFF " <<  a << ' ' << b << endl;
			int g = a;
			a = nx[a][b].first;
			b = nx[g][b].second;
		}*/
	}
	return 0;
}