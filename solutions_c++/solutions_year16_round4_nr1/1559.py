#include <cstdio>
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <unordered_map>
#include <queue>
#include <vector>

using namespace std;

typedef pair<int,int> PI;
const int dr[] = {-1,0,1,0};
const int dc[] = {0,1,0,-1};
typedef long long LL;

char what[8];

bool possible( vector<int> p ) {
	int n = p.size();
	
	while( n > 1 ) {
		int index = 0;
		for( int i = 0; i < n; i += 2, ++index ) {
			
			if( what[p[i]] == what[p[i+1]] ) return false;
			char a = what[p[i]];
			char b = what[p[i+1]];
			if( (a == 'R' && b == 'S') ||
				(a == 'S' && b == 'P') ||
				(a == 'P' && b == 'R') ) {
				
				p[index] = p[i];
			}
			else p[index] = p[i+1];
			
		}
		n /= 2;
	}
	return true;
}

int main() {
	int cases;
	
	cin >> cases;
	for( int caseid = 1; caseid <= cases; ++caseid ) {
		cout << "Case #" << caseid << ": ";
		int N, R, P, S;
		cin >> N >> R >> P >> S;
		
		vector<int> p;
		for( int i = 0; i < (1<<N); ++i ) {
			p.push_back(i);
		}
		
		for( int i = 0; i < R; ++i ) {
			what[i] = 'R';
		}
		for( int i = 0; i < P; ++i ) {
			what[R+i] = 'P';
		}
		for( int i = 0; i < S; ++i ) {
			what[R+P+i] = 'S';
		}
		
		string res = "";
		
		do {
			if( possible( p ) ) {
				string tmp;
				for( int i = 0; i < (1<<N); ++i ) {
					tmp += what[p[i]];
				}
				if( res.size() == 0 || tmp < res ) res = tmp;
			}
		} while( next_permutation( p.begin(), p.end() ) );
		
		if( res.size() == 0 ) cout << "IMPOSSIBLE\n";
		else cout << res << endl;
	}
	return 0;	
}
