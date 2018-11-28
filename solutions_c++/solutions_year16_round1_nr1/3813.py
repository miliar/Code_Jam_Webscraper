#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

#define MOD 1000000007
#define MAXN 100001

#define PRIME 1000008259

using namespace std;


int main(){
    freopen( "input.txt", "r", stdin );
    freopen( "output.txt", "w", stdout );
	
	int tc; cin >> tc;
	
	for (int tc_i = 0; tc_i < tc; tc_i++) {
		string s; cin >> s;
		string res = "";
		int maxIndex = -1;
		int m[2000] = {2000};
		vector< pair<int, int> > arr;
		
		for (int i = 0; i < s.size(); i++) {
			if (i == 0) {
				m[i] = i;
			}
			else {
				if (s[m[i - 1]] <= s[i]) {
					m[i] = i;
				}
				else {
					m[i] = m[i - 1];
				}
			}
		}
		
		int last = s.size() - 1;

		while (last >= 0) {
			int mIndex = m[last];
			
			res += s[mIndex];
			
			if (mIndex < s.size() - 1) {
				arr.push_back(make_pair(mIndex + 1, last));
			}
			
			last = mIndex - 1;
		}
		
		for (int i = arr.size() - 1; i >= 0; i--) {
			for (int j = arr[i].first; j < arr[i].second + 1; j++) {
				res += s[j];
			}
		}
		
		cout << "Case #" << (tc_i + 1) << ": ";
		cout << res;
		cout << endl;
	}
    return 0;
}