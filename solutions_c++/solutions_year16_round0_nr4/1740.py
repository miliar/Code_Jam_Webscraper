#include <bits/stdc++.h>
#include <tr1/unordered_map>

using namespace std;
using namespace tr1;

typedef long long int64;
typedef unsigned long long uint64;

int main(){
	ios::sync_with_stdio(false);
	int t, s, k, c, w = 1;

	cin >> t;
	while( t-- ){
		cin >> k >> c >> s;
		cout << "Case #" << w++ << ":";
		vector < uint64 > ans;
		for(int i = 0; i < k; i++){
			uint64 at = uint64(i);
			for( int j = 0; j < c-1; j++ ){
				at = at*k;
			}
			ans.push_back(at);
		}
		for(int i = 0; i < ans.size(); i++){
			cout << " " << ans[i]+1LL;
		}
		cout << '\n';
	}
	return 0;
}