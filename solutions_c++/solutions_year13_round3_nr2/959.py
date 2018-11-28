#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#define P pair< int, int >
using namespace std;

ifstream fin( "B-small-attempt0.in" );
ofstream fout( "B1.out" );
#define cin fin
#define cout fout


struct node{
	int x, y, jmp;
	node( int _x, int _y, int _jmp ){
		x = _x, y = _y, jmp = _jmp;
	}
	bool operator < ( const node& m ) const{
		if( x != m.x )
			return x < m.x;
		if( y != m.y )
			return y < m.y;
		return jmp < m.jmp;
	}
};

set< node > st;
int res = 0;
char p[600];
int ptr = 0;
int X, Y;
int dr[4][2] = { {1, 0}, {-1, 0}, {0, 1}, {0, -1}};
char ch[] = {'E', 'W', 'N', 'S' };

int dfs( int x, int y, int jmp ){
	//cout << x << ' ' << y << ' ' << jmp << endl;
	if( x == X && y == Y ){
	/*	cout << x << ' ' << y << ' ' << jmp << ' ' << ptr << endl;
		for( int j = 0; j < ptr; j++ )
			cout << p[j];
		cout << endl;
	*/
		return 1;
	}
	if( abs( x ) > 200 || abs( y ) > 200 || jmp > 200 )
		return 0;
	if( jmp > 500 )
		return 0;
	if( st.count( node( x, y, jmp ) ) )
		return 0;
	st.insert( node( x, y, jmp ) );
	for( int i = 0; i < 4; i++ ){
		int nx = x + jmp * dr[i][0];
		int ny = y + jmp * dr[i][1];
		p[ptr++] = ch[i];
		if( dfs( nx, ny, jmp + 1 ) )
			return 1;
		ptr--;
	}
	return 0;
}

int test, T = 1;

int main()
{
	for( cin >> test; test--; ){
		cerr << test << endl;
		cin >> X >> Y;
		ptr = 0;
		st.clear();
		bool rs = dfs( 0, 0, 1 );
		if( !rs )
			cerr << "naaaaaa " << endl;
		int cx = 0, cy = 0;
		for( int i = 0; i < ptr; i++ ){
			for( int j = 0; j < 4; j++ )
				if( ch[j] == p[i] ){
					cx += ( i + 1 ) * dr[j][0];
					cy += ( i + 1 ) * dr[j][1];
				}
		}
		cout << "Case #" << T++ << ": ";
		for( int i = 0; i < ptr; i++ )
			cout << p[i];
		cout << endl;
	}
	return 0;
}