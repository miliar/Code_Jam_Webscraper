#include <bits/stdc++.h>
using namespace std;

void single_test() {
	int n, r, p, s;
	cin >> n >> r >> p >> s;
	int tot = (1<<n);
	vector<char> pool;
	for(int i=0; i<r; ++i) pool.push_back('R');
	for(int i=0; i<p; ++i) pool.push_back('P');
	for(int i=0; i<s; ++i) pool.push_back('S');
	string ans = "Z";
	vector<int> order(tot);
	for(int i=0; i<tot; ++i)
		order[i] = i;
	do {
		bool ok = true;
		vector<char> tmp(tot);
		for(int i=0; i<tot; ++i)
			tmp[i] = pool[order[i]];
		while(ok && tmp.size()>1) {
			vector<char> t;
			for(int i=0; i<(int)tmp.size(); i+=2) {
				if(tmp[i]==tmp[i+1]) {
					ok = false;
					break;
				}
				char a = min(tmp[i], tmp[i+1]);
				char b = max(tmp[i], tmp[i+1]);
				if(a=='P' && b=='R') {
					t.push_back('P');
				} else if(a=='P' && b=='S') {
					t.push_back('S');
				} else if(a=='R' && b=='S') {
					t.push_back('R');
				}
			}
			tmp = t;
		}
		if(ok) {
			string ans2(tot, ' ');
			for(int i=0; i<tot; ++i) ans2[i] = pool[order[i]];
			if(ans2<ans) {
				ans = ans2;
			}
		}
	} while(next_permutation(order.begin(), order.end()));
	if(ans=="Z") {
		cout << "IMPOSSIBLE" << endl;
	} else {
		cout << ans << endl;
	}
	return;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.precision(10);
	cout << fixed;
	int t;
	cin >> t;
	for(int i=1; i<=t; ++i) {
		cout << "Case #" << i << ": ";
		single_test();
	}
	return 0;
}
