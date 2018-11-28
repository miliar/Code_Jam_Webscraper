#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <iostream>
#include <sstream>
#include <set>
#include <map>
#include <string.h>
#include <queue>
#include <utility>
#include <time.h>
#include <string.h>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for( int C = 1; C <= T; C ++ ){
		string str;
		int n;
		cin >> str >> n;
		map<int,int> m;
		for( int i = 0, len = 0; i <= str.size(); i ++ ){
			if( str[i] == 'a' || str[i] == 'e' || str[i] == 'i' || str[i] == 'o' || str[i] == 'u' || str[i] == 0 ){
				if( len >= n ){
					m[i-1] = len;
				}
				len = 0;
			}
			else
				len ++;
		}
		long long ret = 0;
		for( int i = 0; i < str.size(); i ++ ){
			map<int,int>::const_iterator it = m.upper_bound(i+n-2);
			if( it != m.end() ){
				int s = max(i+n, it->first+1-it->second+n);
//				printf( "%d %d %d\n", s, it->first, it->second );
				if( s <= str.size() )
					ret += str.size() + 1 - s;
			}
		}
		cout << "Case #" << C << ": " << ret << endl;
	}
	return 0;
}
