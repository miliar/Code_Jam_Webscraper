#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <sstream>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef set<ll> sll;

void solve(int k, int c, int s) {
	if(s*c < k) {
		cout << "IMPOSSIBLE" << endl;
		return;
	}
	for(int i = 0;i < k; i+=c) {
		ll pos(0);
		for(ll l = i;l < i+c; ++l) {
			pos = pos*k + min(l,(ll)(k-1));
		}
		cout << " " << (pos+1);
	}
	cout << endl;
}

int main() {
	int T;
	cin >> T;
	for(int t = 1;t <= T; ++t) {
		int K,C,S;
		cin >> K >> C >> S;
		cout << "Case #" << t << ":";
		solve(K,C,S);
	}
	return 0;
}