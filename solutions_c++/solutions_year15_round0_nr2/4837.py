#include <iostream>
#include <map>
#include <climits>
using namespace std;

short helper(const map<short, short>& count, const short n) {
	short result = 0;
	for(auto& i : count)
		result += ((i.first - 1) / n) * i.second;
	return result;
}

int main() {
	freopen("B-small-attempt1.in", "r", stdin);
    freopen("B-small-attempt1.ou", "w", stdout);
	ios_base::sync_with_stdio(false);
	short T;
	cin >> T;
	for(short D, cases = 1; cin >> D; cases++) {
		map<short, short> count;
		short minute = SHRT_MAX;
		for(short i = 0, j; i < D; i++) {
			cin >> j;
			count[j]++;
		}
		for(auto i = 1; i <= (*count.rbegin()).first; i++) {
			auto temp = helper(count, i) + i;
			if(temp < minute)
				minute = temp;
		}
		cout << "Case #" << cases << ": " << minute << endl;
	}
	return 0;
}