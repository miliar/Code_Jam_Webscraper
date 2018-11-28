#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#define P pair< char, int >
using namespace std;

int n;
vector< char > arrC[1000];
vector< int > arrI[1000];

ifstream fin( "A2.in" );
ofstream fout( "A2.out" );
#define cin fin
#define cout fout

void getOrder( string s, int idx ){
	vector< P > ret;
	arrC[idx].clear();
	arrI[idx].clear();
	for( int i = 0; i < s.length(); i++ ){
		arrC[idx].push_back( s[i] );
		int j = i;
		while( j < s.length() && s[j] == s[i] )
			j++;
		arrI[idx].push_back( j - i );
		i = j - 1;
	}
}



int main()
{
	int test;
	cin >> test;
	for( int T = 1; T <= test; T++ ){
		cin >> n;
		for( int i = 0; i < n; i++ ){
			string s;
			cin >> s;
			getOrder( s, i );
		}
		bool res = true;
		for( int i = 1; i < n; i++ )
			if( arrC[i] != arrC[i - 1] ){
				res = false;
				break;
			}
		cout << "Case #" << T << ": ";
		if( res == false )
			cout << "Fegla Won" << endl;
		else{
			int ret = 0;
			for( int i = 0; i < arrC[0].size(); i++ ){
				int best = 10000000;
				for( int j = 1; j <= 100; j++ ){
					int sum = 0;
					for( int k = 0; k < n; k++ )
						sum += abs( arrI[k][i] - j );
					best = min( best, sum );
				}
				ret += best;
			}
			cout << ret << endl;
		}
	}
	return 0;
}