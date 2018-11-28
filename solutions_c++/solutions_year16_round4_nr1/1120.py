#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <memory>
#include <bitset>
#include <cassert>

using namespace std;
using ll = long long;
#define FOR(i,a,b) for(ll i=(a); i<(b); ++i)


static char mapping[] = {'R', 'P', 'S'};
static int ord[] = {1,0,2};

static int a[] = {0,0,0};

vector<char> generate(char from, int steps) {
	if(steps == 1) {
		switch(from) {
			case 'R':
				return {'R','S'};
			case 'S':
				return {'P','S'};
			case 'P':
				return {'P','R'};
		}
	} else {
		auto b = generate(from, 1);
		auto b1 = generate(b[0], steps-1), b2 = generate(b[1], steps-1);
		if(b2 < b1) swap(b1, b2);
		for(auto x : b2)
			b1.push_back(x);
		return b1;
	}
}

int main() {
	ll T; cin >> T;
	FOR(t,0,T) {
		cout << "Case #" << t+1 << ": ";
		int n, r, p, s;
		cin >> n >> r >> p >> s;
		vector<vector<char>> res(3);
		res[0] = generate('R', n);
		res[1] = generate('S', n);
		res[2] = generate('P', n);
		sort(begin(res),end(res));
		for(auto x : res) {
			if(count(begin(x),end(x),'R') != r ||
			   count(begin(x),end(x),'P') != p ||
			   count(begin(x),end(x),'S') != s) continue;
			for(char c : x) cout << c;
			res.clear();
			break;
		}
		if(res.size()) cout << "IMPOSSIBLE";
		cout << endl;
	}
}
