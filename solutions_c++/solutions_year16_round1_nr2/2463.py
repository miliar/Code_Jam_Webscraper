#include <cstdio>
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <vector>

using namespace std;

vector< vector<int> > list;
int N;

int x[50][50];

bool can_apply_row( int r, const vector<int>& v ) {
	for( int c = 0; c < r; ++c ) {
		if( x[r][c] == -1 ) continue;
		if( x[r][c] != v[c] ) return false;
	}
	return true;
}

bool can_apply_col( int c, const vector<int>& v ) {
	for( int r = 0; r < c; ++r ) {
		if( x[r][c] == -1 ) continue;
		if( x[r][c] != v[r] ) return false;
	}
	return true;
}

void apply_row( int k, const vector<int>& v, bool full = false ) {
	for( int c = (!full?k:0); c < N; ++c ) {
		if( full ) assert( x[k][c] == -1 || x[k][c] == v[c] );
		x[k][c] = v[c];
	}
}

void apply_col( int k, const vector<int>& v, bool full = false) {
	for( int r = (!full?k:0); r < N; ++r ) {
		if( full ) assert( x[r][k] == -1 || x[r][k] == v[r] );
		x[r][k] = v[r];
	}
}

void undo_apply_row( int k ) {
	for( int c = k; c < N; ++c ) {
		x[k][c] = -1;
	}
}

void undo_apply_col( int k ) {
	for( int r = k; r < N; ++r ) {
		x[r][k] = -1;
	}
}

bool f( int k, int index ) {
	//printf( "%d %d\n", k, index );
	
	if( k == N ) return true;
	
	int m = list.size();
	assert( index < m );

	int min_index1 = index;
	int min_index2 = -1;
	for( int i = index+1; i < m; ++i ) {
		if( list[i][k] < list[min_index1][k] ) {
			min_index1 = i;
			min_index2 = -1;
		} else if( list[i][k] == list[min_index1][k] ) {
			min_index2 = i;
		}
	}
	
	if( min_index2 == -1 ) {
		swap( list[index], list[min_index1] );
		if( can_apply_row( k, list[index] ) ) {
			apply_row( k, list[index] );
			if( f( k+1, index+1 ) ) {
				apply_row( k, list[index], true );
				return true;
			}
			undo_apply_row( k );
		}
		if( can_apply_col( k, list[index] ) ) {
			apply_col( k, list[index] );
			if( f( k+1, index+1 ) ) {
				apply_col( k, list[index], true );
				return true;
			}
			undo_apply_col( k );
		}
	} else {
		swap( list[index], list[min_index1] );
		swap( list[index+1], list[min_index2] );
		
		if( can_apply_row( k, list[index] ) && can_apply_col( k, list[index+1] ) ) {
			apply_row( k, list[index] );
			apply_col( k, list[index+1] );
			if( f( k+1, index+2 ) ) { 
				apply_row( k, list[index], true );
				apply_col( k, list[index+1], true );
				return true;
			}
			undo_apply_row( k );
			undo_apply_col( k );
		}
		
		if( can_apply_row( k, list[index+1] ) && can_apply_col( k, list[index] ) ) {
			apply_row( k, list[index+1] );
			apply_col( k, list[index] );
			if( f( k+1, index+2 ) ) {
				apply_row( k, list[index+1], true );
				apply_col( k, list[index], true );
				return true;	
			}
			undo_apply_row( k );
			undo_apply_col( k );
		}
	} 
	return false;						
}

int main() {
	int T;
	scanf( "%d", &T );

	for( int t = 0; t < T; ++t ) {
		printf( "Case #%d:", t+1 );
		scanf( "%d", &N );
		assert( 2 <= N && N <= 50 );
		list.resize(2*N-1);
		for( int i = 0; i < 2*N-1; ++i ) {
			list[i].resize( N );
			for( int j = 0; j < N; ++j ) {
				scanf( "%d", &list[i][j] );
			}
		}
		for( int i = 0; i < N; ++i ) {
			for( int j = 0; j < N; ++j ) {
				x[i][j] = -1;
			}
		}
		assert( f(0,0) );

		/*
		printf( "x:\n" );
		for( int i = 0; i < N; ++i ) {
			for( int j = 0; j < N; ++j ) {
				printf( " %d", x[i][j] );
			}
			putchar('\n');
		}
		*/
		
		
		multiset<vector<int>> s;
		for( int i = 0; i < N; ++i ) {
			vector<int> a, b;
			for( int j = 0; j < N; ++j ) {
				assert( x[i][j] != -1 );
				a.push_back( x[i][j] );
				b.push_back( x[j][i] );
			}
			s.insert( a );
			s.insert( b );
		}
		
		/*
		printf( "have:\n" );
		for( auto y : s ) {
			for( int x : y ) printf( " %d", y );
			putchar('\n');
		}
		*/
		
		assert( s.size() == 2*N );
		for( int i = 0; i < 2*N-1; ++i ) {
			auto iter = s.find( list[i] );
			
			assert( iter != s.end() );
			s.erase( iter );			
		}
		assert( s.size() == 1 );
		vector<int> res = *(s.begin()); 
		for( int i = 0; i < N; ++i ) {
			printf( " %d", res[i] );
		}
		putchar('\n');
	}
	return 0;	
}
