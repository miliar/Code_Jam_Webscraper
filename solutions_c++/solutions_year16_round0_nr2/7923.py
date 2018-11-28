#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>

#define MAXN 105

using namespace std;

char text[MAXN];
int t, n, ans;

void print( vector <char> tmp ) {
	for ( int k = 0; k < tmp.size(); ++k ) {
		cout << tmp[k];
	}
	cout << endl;
}

struct state {
	int level;
	vector <char> f;
};

int main( ) {
	
	scanf( "%d", &t );
	
	for ( int T = 0; T < t; ++T ) {
		
		scanf( "%s", text );
		
		state start;
		
		n = strlen( text );
		
		for ( int i = 0; i < n; ++i ) {
			start.f.push_back( text[i] );
		}
		
		start.level = 0;
		
		ans = 0;
		
		queue < state > q;
		set < vector<char> > s;
		
		q.push( start );
		s.insert( start.f );
		
		bool found = false;
		
		while ( !q.empty() ) {
			
			state top = q.front();
			q.pop();
			
			
			found = true;
			for ( int z = 0; z < top.f.size() && found; ++z ) {
				if ( top.f[z] == '-' ) {
					found = false;
					break;
				}
			}
			
			if ( found ) {
				ans = top.level;
				break;
			}
			
			++top.level;
			
			
			int right = top.f.size();
			
			while ( right > 0 && top.f[right-1] == '+' ) {
				--right;
			}
			
			//print( top.f );
			
			for ( int i = 0 ; i < right; ++i ) {
				state next = top;
				
				for ( int j = 0; j <= i; ++j ) {
					if ( next.f[j] == '-' ) {
						next.f[j] = '+';
					}else {
						next.f[j] = '-';
					}					
				}
				
				int first = 0;
				int last = i;
				while ( first < last ) {
					char tmp = next.f[first];
					next.f[first] = next.f[last];
					next.f[last] = tmp;
					++first;
					--last;
				}
				
				if ( s.find( next.f) == s.end() ) {
					q.push( next );
					s.insert( next.f );
				}
				
			}
			
		}
		
		
		printf( "Case #%d: %d\n" , T+1, ans );
		
	}
	
	return 0;
	
}