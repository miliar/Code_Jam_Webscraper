#include <cassert>
#include <string>
#include <sstream>
#include <iostream>
#include <deque>
#include <cctype>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <cstring>
#include <bitset>

using namespace std;

typedef pair<int,int> PI;
typedef long long LL;

string s[204];
map<string,int> dict;
vector<int> words[204];
bitset<4004> english, french;

int main() {
	int cases;

	cin >> cases;

	for( int caseno = 1; caseno <= cases; ++caseno ) {
		cout << "Case #" << caseno << ": ";
		int N;
		cin >> N;
		while( getchar() != '\n' );
		
		for( int i = 0; i < N; ++i ) {			
			getline( cin, s[i] ); 
		}
		//cerr << "N= " << N << endl;
		string t;
		dict.clear();

		for( int i = 0; i < N; ++i ) {
			words[i].clear();
			istringstream str( s[i] );
			while( str >> t ) {
				auto iter = dict.find( t );
				if( iter == dict.end() ) {
					int cnt = dict.size();
					dict[t] = cnt;					
					words[i].push_back(cnt);
				} else {
					words[i].push_back(iter->second);
				}
			}
		}
		assert( dict.size() < 4004 );
		
		int res = 1000000000;
		
		for( int i = (1<<(N-2))-1; i >= 0; --i ) {
			english.reset();
			french.reset();
			for( int j = 0; j < (int)words[0].size(); ++j ) {
				english.set(words[0][j] );
			}
			for( int j = 0; j < (int)words[1].size(); ++j ) {
				french.set(words[1][j] );
			}
			
			for( int j = 0; j < N-2; ++j ) {
				for( int k = 0; k < (int)words[2+j].size(); ++k ) {
					if( i & (1<<j) ) {
						english.set(words[2+j][k]);
					} else {
						french.set(words[2+j][k]);
					}					
				}
			}
			
			int intersection = 0;
			for( int j = 0; j < (int)dict.size(); ++j ) {
				if( english.test(j) && french.test(j) ) {
					++intersection;
				}
			}
			 
			res = min( res, intersection );			
		}
		cout << res << endl;
	}
	return 0;
}

