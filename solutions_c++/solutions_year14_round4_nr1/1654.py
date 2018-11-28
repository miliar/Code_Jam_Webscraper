#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstdio>
#include <map>
#include <sstream>
#include <algorithm>
using namespace std;

int T, nCase = 1;
int N, X, s[10001];

int main()
{
	cin >> T;
	while (T--) {
		cin >> N >> X;
		for (int i=0;i<N;++i) cin >> s[i] ;
		sort(s, s+N);
		reverse(s, s+N);
		
		int ans = 0;
		for (int i=0;i<N;++i) {
			if ( s[i] == 0 ) continue;
			int r = X - s[i];
			for ( int j=i+1;j<N;++j ) {
				if ( s[j] <= r  && s[j] > 0) {
					s[j] = 0; break;
				}
			}
			++ ans ;
		}
		
		cout << "Case #" << nCase ++ << ": " << ans << endl;
	}
	return 0;
}