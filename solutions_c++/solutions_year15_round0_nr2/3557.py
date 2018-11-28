#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>
#include <queue>
#include <unordered_map>
#include <unordered_set>

using namespace std;

template<typename T> std::ostream& operator<<(std::ostream& str, const std::vector<T>& v) { str << "["; for(auto n : v) str << n << ", "; str << "]"; return str; }

#define debug(x) cout <<  #x  << ": " << x << endl

bool possible(int time, const vector<int>& p) {
	for (int specials=0; specials<time; ++specials) {
		int max_portion = time - specials;
		int needed_specials = 0;

		for(auto pi : p) {
			while(pi > max_portion) {
				++needed_specials;
				pi -= max_portion;
			}
		}

		if(needed_specials <= specials)
			return true;
	}

	return false;
}

int main() {
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);

	int t;
	cin >> t;

	for(int c=1; c<=t; ++c) {
		int d;
		cin >> d;

		vector<int> p(d);
		for(auto& pi : p) cin >> pi;

		int upper=1001,lower=0;
		while(lower+1 < upper) {
			int mid = lower + (upper-lower)/2;

			//debug(mid);
			//debug(possible(mid,p));
			if(!possible(mid, p))
				lower = mid;
			else
				upper = mid;
		}

		cout << "Case #" << c << ": " << lower+1 << endl;
	}	
}