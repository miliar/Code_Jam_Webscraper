#include <bits/stdc++.h>

using namespace std;

int main() {
	
	freopen( "in", "r", stdin );
	freopen( "out", "w", stdout );
	
	int t;
	cin >> t;
	
	for( int w = 1; w <= t; ++w ){
		string line;
		cin >> line;
		
		int moves = 0;
		
		char curr = line[0];
		
		for( int i = 1; i < (int) line.size(); ++i ){
			if( line[i] != curr ){
				++moves;
				curr = line[i];
			}
		}
		
		if( curr == '-' ){
			++moves;
		}
		
		cout << "Case #" << w << ": " << moves << endl;
		
	}
	

	return 0;
}
