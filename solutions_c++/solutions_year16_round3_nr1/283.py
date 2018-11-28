#include <iostream>
#include <queue>
#include <string>
#include <fstream>
#define P pair< int, int >

using namespace std;

ifstream fin( "A2.in" );
ofstream fout( "A2.out" );
#define cin fin
#define cout fout
priority_queue< P > q;

int main()
{
	int test, n;
	cin >> test;
	for( int T = 1; T <= test; T++ ){
		while( !q.empty() )
			q.pop();
		cin >> n;
		int sum = 0;
		for( int i = 0; i < n; i++ ){
			int a;
			cin >> a;
			sum += a;
			q.push( P( a, i ) );
		}
		cout << "Case #" << T << ":"; 
		while( !q.empty() ){
			string out;
			P mx1 = q.top();
			q.pop();
			P mx2 = q.top();
			q.pop();
			out += (char)( 'A' + mx1.second );
			mx1.first--;
			sum--;
			if( mx2.first > ( sum - mx2.first ) ){
				out += (char)( 'A' + mx2.second );
				mx2.first--;
				sum--;
			}
			if( mx1.first )
				q.push( mx1 );
			if( mx2.first )
				q.push( mx2 );
			cout << ' ' << out;
		}
		cout << endl;
	}
	return 0;
}