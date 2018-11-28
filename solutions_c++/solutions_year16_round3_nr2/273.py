#include <iostream>
#include <vector>
#include <fstream>
#define INF 1000000
#define P pair< int, int >
using namespace std;

ifstream fin( "B2.in" );
ofstream fout( "B2.out" );
#define cin fin
#define cout fout

long long B, M;
vector< P > v;
bool g[100][100];
long long state[100];
bool invalid[100];

int main()
{
	int test;
	cin >> test;
	for( int T = 1; T <= test; T++ ){
		memset( state, 0, sizeof state );
		memset( g, false, sizeof g );
		memset( invalid, false, sizeof invalid );
		cin >> B >> M;
		v.clear();
		for( int i = 0; i < B; i++ )
			for( int j = i + 1; j < B; j++ )
				v.push_back( P( i, j ) );
		int sz = v.size();
		bool has = false;
		cout << "Case #" << T << ": ";
		if( M > ( 1LL << ( B - 2 ) ) ){
			cout << "IMPOSSIBLE" << endl;
		}
		else{
			state[B - 1] = 1;
			int cnt = B - 2;
			long long sum = 1;
			long long curVal = 1;
			while(cnt){
			//while( sum + curVal <= M ){
				state[cnt] = curVal;
				sum += curVal;
				for( int i = cnt + 1; i < B; i++ )
					g[cnt][i] = 1;
				cnt--;
				curVal <<= 1 ;
			}
			long long p = M;
			//while( p ){
			for( int i = 1; i < B; i++ )
				if( state[i] > 0 && state[i] <= p ){
					//cout << state[i] << ' ' << p << endl;
					p -= state[i];
					g[0][i] = true;
				}
			//}
			cout << "POSSIBLE" << endl;
			for( int i = 0; i < B; i++ ){
				for( int j = 0; j < B; j++ )
					cout << g[i][j];
				cout << endl;
			}
		}
	}
	return 0;
}