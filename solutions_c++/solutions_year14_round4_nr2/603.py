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

	int n;
	vector<int> orig;
	int L[1024], R[1024];

	void main(){
		ios_base::sync_with_stdio(false);
		register int i, j;
		int T;
		cin >> T;
		for(int t = 1; t <= T; ++ t) {
			cin >> n;
			orig.clear();
			memset(L, 0, sizeof L);
			memset(R, 0, sizeof R);
			for(i = 0; i < n; ++ i) {
				int x;
				cin >> x;
				orig.push_back(x);
			}
			for(i = 0; i < n; ++ i) {
				for(j = 0; j < i; ++ j) {
					if(orig[j] > orig[i]) ++ L[i];
				}
				for(j = i; j < n; ++ j) {
					if(orig[i] < orig[j]) ++ R[i];
				}
			}
			int ans = 0;
			for(i = 0; i < n; ++ i) ans += min(L[i], R[i]);
			cout << "Case #" << t << ": " << ans << endl;
		}
	}
}

int main(){
	Solve::main();
	return 0;
}
