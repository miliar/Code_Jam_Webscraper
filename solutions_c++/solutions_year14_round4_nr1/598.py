#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<climits>
#include<cassert>
#include<cctype>
#include<ctime>
#include<ciso646>
#include<cstddef>
#include<iostream>
#include<fstream>
#include<functional>
#include<iomanip>
#include<string>
#include<map>
#include<vector>
#include<deque>
#include<set>
#include<queue>
#include<stack>
#include<algorithm>
#include<list>
#include<numeric>
#include<complex>
#include<new>

using namespace std;

typedef vector<int> vi;
typedef map<int, int> mii;
typedef set<int> si;
typedef queue<int> qi;
typedef stack<int> sti;
typedef pair<int, int> pii;

namespace Solve {

	multiset<int> S;
	multiset<int>::iterator it, itf;

	template <class T> inline bool _max(T &ans, const T &comp) {
		if (ans < comp) {
			ans = comp;
			return true;
		}
		return false;
	}

	template <class T> inline bool _min(T &ans, const T &comp) {
		if (ans > comp) {
			ans = comp;
			return true;
		}
		return false;
	}

	void main(){
		ios_base::sync_with_stdio(false);
		register int i, j;
		int T;
		cin >> T;
		for(int t = 1; t <= T; ++ t) {
			int n, x;
			cin >> n >> x;
			S.clear();
			for(i = 0; i < n; ++ i) {
				int w;
				cin >> w;
				S.insert(w);
			}
			int cnt = 0;
			while(S.size() > 1) { // Combine two files.
				it = S.begin();
				int left = x - *it;
				itf = S.upper_bound(left);
				if(itf == S.begin()) { // No available selection
					break;
				}
				-- itf;
				if(itf == S.begin()) { // No available selection
					break;
				}
				S.erase(itf);
				S.erase(S.begin()); // it is invalid now.
				++ cnt;
			}
			cout << "Case #" << t << ": " << cnt + S.size() << endl;
		}
	}
}

int main(){
	Solve::main();
	return 0;
}
