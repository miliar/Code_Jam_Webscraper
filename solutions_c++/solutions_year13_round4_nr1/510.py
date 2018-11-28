#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main()
{
    __int64 T;
    cin >> T;
    for ( __int64 test = 1; test <= T; test++ ) {
		__int64 N, M;
		cin >> N >> M;
		vector<__int64> v(N,0);
		__int64 ex = 0;
		for ( __int64 i = 0; i < M; i++ ) {
			__int64 o, e, t;
			cin >> o >> e >> t;
			__int64 d = e-o;
			ex += (N+N-d+1)*d/2*t;

			for ( __int64 i = o; i < e; i++ ) {
				v[i]+=t;
			}
		}

		__int64 a = 0;
		while ( 1 ) {
			__int64 c = 0;
			while ( c < v.size() && v[c] == 0 ) c++;
			if ( v.size() == c ) break;

			while ( 1 ) {
				__int64 s = c;
				while ( c < v.size() && v[c] ) {
					v[c]--;
					c++;
				}
				__int64 d = c-s;
				a += (N+N-d+1)*d/2;

				while ( c < v.size() && v[c] == 0 ) c++;
				if ( v.size() == c ) break;
			}
		}

        printf( "Case #%d: %lld\n", test, ex-a );
    }
    return 0;
}
