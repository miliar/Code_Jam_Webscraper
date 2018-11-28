#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <map>
using namespace std;
const int MAXN = 100 + 10;

map<int, int> mp;
map<int, int>::iterator it;
int n, m;

int main() {
	freopen( "B.out", "w+", stdout );
	int t, a, b, c;
	scanf( "%d", &t );
	for( int ncas = 1; ncas <= t; ++ncas ) {
		vector<int> vec;
		mp.clear();
		printf( "Case #%d:", ncas );
		scanf( "%d", &n );
		for( int i = 0; i < 2 * n - 1; ++i ) {
			for( int j = 0; j < n; ++j ) {
				scanf( "%d", &a );
				++mp[a];
			}
		}
		for( it = mp.begin(); it != mp.end(); ++it ) {
			if( it->second % 2 ) vec.push_back( it->first );
		}
		sort( vec.begin(), vec.end() );
		for( int i = 0; i < vec.size(); ++i ) printf( " %d", vec[i] );
		puts( "" );
	}
	return 0;
}
