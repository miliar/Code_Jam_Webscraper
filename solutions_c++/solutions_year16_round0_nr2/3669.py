#include <bits/stdc++.h>
using namespace std;

int single_test() {
	string s;
	cin >> s;
	int n = s.size();
	vector<int> up(n+1, 0);
	vector<int> down(n+1, 0);
	for(int i=0; i<n; ++i) {
		if(s[i]=='+') {
			up[i+1] = min(up[i], down[i]+1);
			down[i+1] = 1 + up[i+1];
		} else {
			down[i+1] = min(down[i], up[i]+1);	
			up[i+1] = 1 + down[i+1];
		}
	}
	int res = up[n];
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
		int res = single_test();
		cout << "Case #" << i << ": " << res << endl;
	}
	return 0;
}
