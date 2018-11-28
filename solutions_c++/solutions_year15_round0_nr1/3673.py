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

int main() {
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);

	int t;
	cin >> t;

	for(int c=1; c<=t; ++c) {
		int smax; string audience;
		cin >> smax >> audience;

		vector<int> s;
		for(auto c : audience) s.push_back(c-'0');

		int invite = 0;
		int crowd = 0;

		for(int shyness=0; shyness<s.size(); ++shyness) {
			auto si = s.at(shyness);

			if(crowd >= shyness) {
				crowd += si;
			} else {
				int needed = (shyness-crowd);
				invite += needed;
				crowd += needed + si;
			}
		}

		cout << "Case #" << c << ": " << invite << endl;
	}	
}