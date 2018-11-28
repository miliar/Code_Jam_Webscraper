#include <bits/stdc++.h>
using namespace std;

vector<int> single_test() {
	int k, c, s;
	cin >> k >> c >> s;
	if(s<k) return vector<int>();
	vector<int> res;
	for(int i=1; i<=k; ++i) res.push_back(i); 
	return res;
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
		vector<int> res = single_test();
		cout << "Case #" << i << ":";
		if(!res.empty()) {
			for(int j: res) cout << ' ' << j;
		} else {
			cout << " IMPOSSIBLE";
		}
		cout << endl;
	}
	return 0;
}
